# DEV config
import os

DEBUG = True
SQLALCHEMY_DATABASE_URI = "sqlite:///data.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False
PROPAGATE_EXCEPTIONS = True
# JWT_SECRET_KEY = os.environ["JWT_SECRET_KEY"]
JWT_SECRET_KEY = "Mike123"
JWT_BLACKLIST_ENABLED = True
JWT_BLACKLIST_TOKEN_CHECKS = [
    "access",
    "refresh",
]  # means blacklist is enabled for access & refresh tokens
# SECRET_KEY = os.environ["APP_SECRET_KEY"]
SECRET_KEY = "Mike123"
BABEL_DEFAULT_LOCALE = "en"
LANGUAGES = {"en": "English", "es_mx": "Mexican Spanish"}
