from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


users = db.Table(
    "users",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
    db.Column("group_id", db.Integer, db.ForeignKey("user_group.id"), primary_key=True),
)


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(100), nullable=False, info={"label": "Name"})
    groups = db.relation("UserGroup", back_populates="role", lazy=True)
    users = db.relation("User", back_populates="role", lazy=True)

    def to_dict(self):
        columns_keys = self.__table__.columns.keys()
        _role = {key: getattr(self, key) for key in columns_keys}
        return _role


class UserGroup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(100), nullable=False, info={"label": "Name"})
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    users = db.relation(
        "User",
        secondary=users,
        lazy="subquery",
        back_populates="groups",
    )
    role = db.relation("Role", back_populates="groups", lazy=True)

    def to_dict(self):
        columns_keys = self.__table__.columns.keys()
        _group = {key: getattr(self, key) for key in columns_keys}
        return _group


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.Unicode(100), nullable=False, info={"label": "Login"})
    first_name = db.Column(
        db.Unicode(100), nullable=False, info={"label": "First name"}
    )
    last_name = db.Column(db.Unicode(100), nullable=False, info={"label": "Last name"})
    birthday = db.Column(db.Date, nullable=False, info={"label": "Birthday"})
    created_at = db.Column(db.DateTime)
    email = db.Column(db.Unicode(255))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    groups = db.relation(
        "UserGroup",
        secondary=users,
        lazy="subquery",
        back_populates="users",
    )
    role = db.relation("Role", back_populates="users", lazy=True)

    def __init__(self, login, first_name, last_name, birthday, created_at, **kwargs):
        self.login = login
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.created_at = created_at
        self.email = kwargs.pop("email", None)

    def to_dict(self):
        columns_keys = self.__table__.columns.keys()
        _user = {key: getattr(self, key) for key in columns_keys}
        return _user
