class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = "4abc2f79f76a85654f25b529ce33ac7e"
    SQLALCHEMY_DATABASE_URI = "postgres://postgres:superuserpassword@localhost/user_manager"