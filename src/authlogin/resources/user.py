import traceback

from flask_restful import Resource
from werkzeug.security import safe_str_cmp
from flask_login import login_user, logout_user, login_required
from flask import request, session
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_refresh_token_required,
    get_jwt_identity,
    jwt_required,
    get_raw_jwt,
    fresh_jwt_required,
)
from flask_babel import gettext
from db import db

from authlogin.schemas.user import UserSchema
from authlogin.models.user import User


user_schema = UserSchema()
user_list_schema = UserSchema(many=True)


class UserRegister(Resource):
    @classmethod
    def post(cls):
        user_json = request.get_json()
        user = user_schema.load(user_json)

        try:
            user.save_to_db()
            return {"message": gettext("SUCCESS_REGISTER_MESSAGE")}, 201
        except:  # failed to save user to db
            traceback.print_exc()
            user.delete_from_db()
            return {"message": gettext("FAILED_TO_CREATE")}, 500


class UserLogin(Resource):
    @classmethod
    def post(cls):
        user_json = request.get_json()
        data = user_schema.load(user_json)

        user = User.find_by_email(data.email)

        if user and safe_str_cmp(user.password, data.password):
                access_token = create_access_token(identity=user.id, fresh=True)
                refresh_token = create_refresh_token(user.id)

                login_user(user)
                return (
                    {"access_token": access_token, "refresh_token": refresh_token},
                    200,
                )
            

        return {"message": gettext("INVALID_CREDENTIALS")}, 401

# TODO gettext
class UserLogout(Resource):
    @classmethod
    @login_required
    def post(cls):
        # user_json = request.get_json()
        # data = user_schema.load(user_json)

        # user = User.find_by_email(data.email)
        
        logout_user()
        return ({"message": gettext("LOGGED_OUT")},200,)
           