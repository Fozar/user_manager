from datetime import date, datetime

import wtforms_json
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_wtf import CSRFProtect

from config import Config
from endpoints import *
from models import db, User, Role

app = Flask(__name__)
app.config.from_object(Config)
wtforms_json.init()
csrf = CSRFProtect(app)

CORS(app)
api = Api(app, decorators=[csrf.exempt])
db.init_app(app)
bcrypt = Bcrypt(app)
jwt_manager = JWTManager(app)

with app.app_context():
    db.create_all()
    if not User.query.filter_by(login="admin").first():
        admin = User(
            login="admin",
            password="admin",
            first_name="admin",
            last_name="admin",
            birthday=date.today(),
            created_at=datetime.utcnow(),
        )
        db.session.add(admin)
        db.session.commit()


@app.after_request
def add_cors(rv):
    rv.headers.add("Access-Control-Allow-Headers", "Content-type")
    rv.headers.add("Access-Control-Allow-Credentials", "true")
    rv.headers.add("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE")
    return rv


api.add_resource(RolesList, "/roles")
api.add_resource(Roles, "/roles/<role_id>")
api.add_resource(RolesMetadata, "/roles/<role_id>/metadata")
api.add_resource(GroupsList, "/groups")
api.add_resource(Groups, "/groups/<group_id>")
api.add_resource(GroupsMetadata, "/groups/<group_id>/metadata")
api.add_resource(UsersList, "/users")
api.add_resource(Users, "/users/<user_id>")
api.add_resource(UsersMetadata, "/users/<user_id>/metadata")
api.add_resource(LoginApi, "/auth/login")

if __name__ == "__main__":
    app.run()
