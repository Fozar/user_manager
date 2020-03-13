from datetime import datetime, timedelta

from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from flask_restful import Resource, abort

from forms import UserForm, UserGroupForm, RoleForm
from models import User, db, UserGroup, Role


class LoginApi(Resource):
    def post(self):
        body = request.get_json()
        user = User.query.filter_by(login=body.get("login")).first()
        if not user:
            response = jsonify({"error": "Login invalid", 'authenticated': False})
            response.status_code = 401
            return response
        auth = user.check_password(body.get("password"))
        if not auth:
            response = jsonify({"error": "Password invalid", 'authenticated': False})
            response.status_code = 401
            return response

        access_token = create_access_token(
            identity=str(user.id), expires_delta=timedelta(days=1)
        )
        response = jsonify({"user": user.to_dict(), "token": access_token})
        response.status_code = 200
        return response


class Users(Resource):
    @jwt_required
    def get(self, user_id):
        user = User.query.filter_by(id=int(user_id)).first()
        if not user:
            abort(404)
        response = jsonify(user.to_dict())
        response.status_code = 200
        return response

    @jwt_required
    def delete(self, user_id):
        user = User.query.filter_by(id=int(user_id))
        if not user:
            abort(404)
        user.first().groups = []
        db.session.flush()
        user.delete()
        db.session.commit()
        return 200

    @jwt_required
    def put(self, user_id):
        user = User.query.filter_by(id=int(user_id)).first()
        if not user:
            abort(404)
        form = UserForm.from_json(request.get_json(), obj=user)
        if not form.validate():
            abort(400)
        columns_keys = User.__table__.columns.keys()
        for field in columns_keys:
            if field in form.data:
                setattr(user, field, form.data[field])
        user.hash_password()
        db.session.commit()
        response = jsonify(user.to_dict())
        response.status_code = 200
        return response


class UsersList(Resource):
    @jwt_required
    def get(self):
        users = [user.to_dict() for user in User.query.all()]
        response = jsonify(users)
        response.status_code = 200
        return response

    @jwt_required
    def post(self):
        form = UserForm(data=request.get_json())
        if not form.validate():
            response = jsonify(form.errors)
            response.status_code = 400
            return response
        user = User(**form.data)
        user.created_at = datetime.utcnow()
        db.session.add(user)
        db.session.commit()
        response = jsonify(**user.to_dict())
        response.status_code = 201
        response.headers.add("Location", f"users/{user.id}")
        return response


class Roles(Resource):
    @jwt_required
    def get(self, role_id):
        role = Role.query.filter_by(id=int(role_id)).first()
        if not role:
            abort(404)
        response = jsonify(role.to_dict())
        response.status_code = 200
        return response

    @jwt_required
    def delete(self, role_id):
        role = Role.query.filter_by(id=int(role_id))
        if not role:
            abort(404)
        role.first().users = []
        role.first().groups = []
        db.session.flush()
        role.delete()
        db.session.commit()
        return 200

    @jwt_required
    def put(self, role_id):
        role = Role.query.filter_by(id=int(role_id)).first()
        if not role:
            abort(404)
        form = RoleForm(data=request.get_json())
        if not form.validate():
            abort(400)
        columns_keys = Role.__table__.columns.keys()
        for field in columns_keys:
            if field in form.data:
                setattr(role, field, form.data[field])
        db.session.commit()
        response = jsonify(role.to_dict())
        response.status_code = 200
        return response


class RolesList(Resource):
    @jwt_required
    def get(self):
        roles = [role.to_dict() for role in Role.query.all()]
        response = jsonify(roles)
        response.status_code = 200
        return response

    @jwt_required
    def post(self):
        form = RoleForm(data=request.get_json())
        if not form.validate():
            abort(400)
        role = Role(**form.data)
        db.session.add(role)
        db.session.commit()
        response = jsonify(**role.to_dict())
        response.status_code = 201
        response.headers.add("Location", f"roles/{role.id}")
        return response


class Groups(Resource):
    @jwt_required
    def get(self, group_id):
        group = UserGroup.query.filter_by(id=int(group_id)).first()
        if not group:
            abort(404)
        response = jsonify(group.to_dict())
        response.status_code = 200
        return response

    @jwt_required
    def delete(self, group_id):
        group = UserGroup.query.filter_by(id=int(group_id))
        if not group:
            abort(404)
        group.first().users = []
        db.session.flush()
        group.delete()
        db.session.commit()
        return 200

    @jwt_required
    def put(self, group_id):
        group = UserGroup.query.filter_by(id=int(group_id)).first()
        if not group:
            abort(404)
        form = UserGroupForm(data=request.get_json())
        if not form.validate():
            abort(400)
        columns_keys = UserGroup.__table__.columns.keys()
        for field in columns_keys:
            if field in form.data:
                setattr(group, field, form.data[field])
        db.session.commit()
        response = jsonify(group.to_dict())
        response.status_code = 200
        return response


class GroupsList(Resource):
    @jwt_required
    def get(self):
        groups = [group.to_dict() for group in UserGroup.query.all()]
        response = jsonify(groups)
        response.status_code = 200
        return response

    @jwt_required
    def post(self):
        form = UserGroupForm(data=request.get_json())
        if not form.validate():
            abort(400)
        group = UserGroup(**form.data)
        db.session.add(group)
        db.session.commit()
        response = jsonify(**group.to_dict())
        response.status_code = 201
        response.headers.add("Location", f"groups/{group.id}")
        return response


class UsersMetadata(Resource):
    @jwt_required
    def get(self, user_id):
        user = User.query.filter_by(id=int(user_id)).first()
        if not user:
            abort(404)
        groups = [group.to_dict() for group in user.groups]
        role = user.role.to_dict() if user.role is not None else None
        response = jsonify({"role": role, "groups": groups})
        response.status_code = 200
        return response

    @jwt_required
    def put(self, user_id):
        user = User.query.filter_by(id=int(user_id)).first()
        if not user:
            abort(404)
        body = request.get_json()
        role_id = body.get("role")
        if role_id is not None:
            role = Role.query.filter_by(id=int(role_id)).first()
            if not role:
                abort(404)
        else:
            role = None
        group_ids = body.get("groups")
        groups = db.session.query(UserGroup).filter(UserGroup.id.in_(group_ids)).all()
        if len(groups) < len(group_ids):
            abort(404)
        user.role = role
        user.groups = groups
        db.session.commit()
        return 200


class GroupsMetadata(Resource):
    @jwt_required
    def get(self, group_id):
        group = UserGroup.query.filter_by(id=int(group_id)).first()
        if not group:
            abort(404)
        users = [user.to_dict() for user in group.users]
        role = group.role.to_dict() if group.role is not None else None
        response = jsonify({"role": role, "users": users})
        response.status_code = 200
        return response

    @jwt_required
    def put(self, group_id):
        group = UserGroup.query.filter_by(id=int(group_id)).first()
        if not group:
            abort(404)
        body = request.get_json()
        role_id = body.get("role")
        if role_id is not None:
            role = Role.query.filter_by(id=int(role_id)).first()
            if not role:
                abort(404)
        else:
            role = None
        user_ids = body.get("users")
        users = db.session.query(User).filter(User.id.in_(user_ids)).all()
        if len(users) < len(user_ids):
            abort(404)
        group.role = role
        group.users = users
        db.session.commit()
        return 200


class RolesMetadata(Resource):
    @jwt_required
    def get(self, role_id):
        role = Role.query.filter_by(id=int(role_id)).first()
        if not role:
            abort(404)
        users = [user.to_dict() for user in role.users]
        groups = [group.to_dict() for group in role.groups]
        response = jsonify({"groups": groups, "users": users})
        response.status_code = 200
        return response

    @jwt_required
    def put(self, role_id):
        role = Role.query.filter_by(id=int(role_id)).first()
        if not role:
            abort(404)
        body = request.get_json()
        user_ids = body.get("users")
        users = db.session.query(User).filter(User.id.in_(user_ids)).all()
        if len(users) < len(user_ids):
            abort(404)
        group_ids = body.get("groups")
        groups = db.session.query(UserGroup).filter(UserGroup.id.in_(group_ids)).all()
        if len(groups) < len(group_ids):
            abort(404)
        role.users = users
        role.groups = groups
        db.session.commit()
        return 200


def get_paginated_list(results, url, start, limit):
    start = int(start)
    limit = int(limit)
    count = len(results)
    if count < start or limit < 0:
        abort(404)
    response = {"start": start, "limit": limit, "count": count}

    if start == 1:
        response["previous"] = ""
    else:
        start_copy = max(1, start - limit)
        limit_copy = start - 1
        response["previous"] = url + f"?start={start_copy}&limit={limit_copy}"

    if start + limit > count:
        response["next"] = ""
    else:
        start_copy = start + limit
        response["next"] = url + f"?start={start_copy}&limit={limit}"

    response["data"] = results[(start - 1) : (start - 1 + limit)]
    return response
