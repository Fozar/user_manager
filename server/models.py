from flask_bcrypt import check_password_hash, generate_password_hash
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

users = db.Table(
    "users",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
    db.Column("group_id", db.Integer, db.ForeignKey("user_group.id"), primary_key=True),
)


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(100), nullable=False)
    groups = db.relation("UserGroup", back_populates="role", lazy=True)
    users = db.relation("User", back_populates="role", lazy=True)

    def __init__(self, name):
        self.name = name

    def to_dict(self):
        columns_keys = self.__table__.columns.keys()
        _role = {key: getattr(self, key) for key in columns_keys}
        return _role


class UserGroup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(100), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"))
    users = db.relation(
        "User", secondary=users, lazy="subquery", back_populates="groups",
    )
    role = db.relation("Role", back_populates="groups", lazy=True)

    def __init__(self, name):
        self.name = name

    def to_dict(self):
        columns_keys = self.__table__.columns.keys()
        _group = {key: getattr(self, key) for key in columns_keys}
        return _group


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.Unicode(50), nullable=False, unique=True)
    password = db.Column(db.Unicode(255), nullable=False)
    first_name = db.Column(db.Unicode(50), nullable=False)
    last_name = db.Column(db.Unicode(50), nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime)
    email = db.Column(db.Unicode(255))
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"))
    groups = db.relation(
        "UserGroup", secondary=users, lazy="subquery", back_populates="users",
    )
    role = db.relation("Role", back_populates="users", lazy=True)

    def __init__(
            self, login, password, first_name, last_name, birthday, created_at, **kwargs
    ):
        self.login = login
        self.password = generate_password_hash(password).decode("utf8")
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.created_at = created_at
        self.email = kwargs.pop("email", None)

    def to_dict(self):
        columns_keys = self.__table__.columns.keys()
        _user = {key: getattr(self, key) for key in columns_keys}
        _user.pop("password")
        return _user

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode("utf8")

    def check_password(self, password):
        return check_password_hash(self.password, password)
