from datetime import datetime

from flask import request, jsonify
from flask_restful import Resource, abort

from forms import UserForm, UserGroupForm, RoleForm
from models import User, db, UserGroup, Role


class Users(Resource):
    @staticmethod
    def get(user_id):
        user = User.query.filter_by(id=int(user_id)).first()
        if not user:
            abort(404)
        response = jsonify(user.to_dict())
        response.status_code = 200
        return response

    @staticmethod
    def delete(user_id):
        user = User.query.filter_by(id=int(user_id))
        if not user:
            abort(404)
        user.first().groups = []
        db.session.flush()
        user.delete()
        db.session.commit()
        return 200

    @staticmethod
    def put(user_id):
        user = User.query.filter_by(id=int(user_id)).first()
        if not user:
            abort(404)
        form = UserForm(data=request.get_json())
        if not form.validate():
            abort(400)
        columns_keys = User.__table__.columns.keys()
        for field in columns_keys:
            if field in form.data:
                setattr(user, field, form.data[field])
        db.session.commit()
        response = jsonify(user.to_dict())
        response.status_code = 200
        return response


class UsersList(Resource):
    @staticmethod
    def get():
        users = [user.to_dict() for user in User.query.all()]
        response = jsonify(users)
        response.status_code = 200
        return response

    @staticmethod
    def post():
        form = UserForm(data=request.get_json())
        if not form.validate():
            abort(400)
        user = User(**form.data)
        user.created_at = datetime.utcnow()
        db.session.add(user)
        db.session.commit()
        response = jsonify(**user.to_dict())
        response.status_code = 201
        response.headers.add("Location", f"users/{user.id}")
        return response


class Roles(Resource):
    @staticmethod
    def get(role_id):
        role = Role.query.filter_by(id=int(role_id)).first()
        if not role:
            abort(404)
        response = jsonify(role.to_dict())
        response.status_code = 200
        return response

    @staticmethod
    def delete(role_id):
        role = Role.query.filter_by(id=int(role_id))
        if not role:
            abort(404)
        role.first().users = []
        role.first().groups = []
        db.session.flush()
        role.delete()
        db.session.commit()
        return 200

    @staticmethod
    def put(role_id):
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
    @staticmethod
    def get():
        roles = [role.to_dict() for role in Role.query.all()]
        response = jsonify(roles)
        response.status_code = 200
        return response

    @staticmethod
    def post():
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
    @staticmethod
    def get(group_id):
        group = UserGroup.query.filter_by(id=int(group_id)).first()
        if not group:
            abort(404)
        response = jsonify(group.to_dict())
        response.status_code = 200
        return response

    @staticmethod
    def delete(group_id):
        group = UserGroup.query.filter_by(id=int(group_id))
        if not group:
            abort(404)
        group.first().users = []
        db.session.flush()
        group.delete()
        db.session.commit()
        return 200

    @staticmethod
    def put(group_id):
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
    @staticmethod
    def get():
        groups = [group.to_dict() for group in UserGroup.query.all()]
        response = jsonify(groups)
        response.status_code = 200
        return response

    @staticmethod
    def post():
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
    @staticmethod
    def get(user_id):
        user = User.query.filter_by(id=int(user_id)).first()
        if not user:
            abort(404)
        groups = [group.to_dict() for group in user.groups]
        role = user.role.to_dict() if user.role is not None else None
        response = jsonify({"role": role, "groups": groups})
        response.status_code = 200
        return response

    @staticmethod
    def put(user_id):
        user = User.query.filter_by(id=int(user_id)).first()
        if not user:
            abort(404)
        data = request.get_json()
        role_id = data["role"]
        if role_id is not None:
            role = Role.query.filter_by(id=int(role_id)).first()
            if not role:
                abort(404)
        else:
            role = None
        group_ids = data["groups"]
        groups = db.session.query(UserGroup).filter(UserGroup.id.in_(group_ids)).all()
        if len(groups) < len(group_ids):
            abort(404)
        user.role = role
        user.groups = groups
        db.session.commit()
        return 200


class GroupsMetadata(Resource):
    @staticmethod
    def get(group_id):
        group = UserGroup.query.filter_by(id=int(group_id)).first()
        if not group:
            abort(404)
        users = [user.to_dict() for user in group.users]
        role = group.role.to_dict() if group.role is not None else None
        response = jsonify({"role": role, "users": users})
        response.status_code = 200
        return response

    @staticmethod
    def put(group_id):
        group = UserGroup.query.filter_by(id=int(group_id)).first()
        if not group:
            abort(404)
        data = request.get_json()
        role_id = data["role"]
        if role_id is not None:
            role = Role.query.filter_by(id=int(role_id)).first()
            if not role:
                abort(404)
        else:
            role = None
        user_ids = data["users"]
        users = db.session.query(User).filter(User.id.in_(user_ids)).all()
        if len(users) < len(user_ids):
            abort(404)
        group.role = role
        group.users = users
        db.session.commit()
        return 200


class RolesMetadata(Resource):
    @staticmethod
    def get(role_id):
        role = Role.query.filter_by(id=int(role_id)).first()
        if not role:
            abort(404)
        users = [user.to_dict() for user in role.users]
        groups = [group.to_dict() for group in role.groups]
        response = jsonify({"groups": groups, "users": users})
        response.status_code = 200
        return response

    @staticmethod
    def put(role_id):
        role = Role.query.filter_by(id=int(role_id)).first()
        if not role:
            abort(404)
        data = request.get_json()
        user_ids = data["users"]
        users = db.session.query(User).filter(User.id.in_(user_ids)).all()
        if len(users) < len(user_ids):
            abort(404)
        group_ids = data["groups"]
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
