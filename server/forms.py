from flask_wtf import FlaskForm
from wtforms.validators import Email
from wtforms_alchemy import model_form_factory

from models import db, User, UserGroup, Role

BaseModelForm = model_form_factory(FlaskForm)


class ModelForm(BaseModelForm):
    @classmethod
    def get_session(cls):
        return db.session


class UserForm(ModelForm):
    class Meta:
        model = User
        validators = {"email": [Email()]}
        csrf = False
        datetime_format = "%Y-%m-%dT%H:%M:%S"


class UserGroupForm(ModelForm):
    class Meta:
        model = UserGroup
        csrf = False


class RoleForm(ModelForm):
    class Meta:
        model = Role
        csrf = False
