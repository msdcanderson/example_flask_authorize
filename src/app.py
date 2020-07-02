from flask import Flask, jsonify, request, g, session
from flask_restful import Api
from flask_jwt_extended import JWTManager
from marshmallow import ValidationError
from flask_babel import Babel
from dotenv import load_dotenv
from datetime import datetime
from flask_login import LoginManager
from flask_authorize import Authorize

from db import db
from ma import ma


app = Flask(__name__)
load_dotenv(".env", verbose=True)
app.config.from_object("default_config")
app.config.from_envvar("APPLICATION_SETTINGS")
babel = Babel(app)
api = Api(app)
jwt = JWTManager(app)
login_manager = LoginManager()
authorize = Authorize(app)


@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err.messages), 400


@app.route("/")
def index():
    return jsonify({"hello": "world"})


if __name__ == "__main__":
    db.init_app(app)
    ma.init_app(app)   

    login_manager.init_app(app)
    from authlogin.models.user import User, Role, Group, UserGroup, UserRole

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


    @app.before_first_request
    def create_tables():
        db.create_all()
        user = User(name="AreaManager", email="areamanager@example.com", password="1234")
        db.session.add(user)
        db.session.commit()
        user1 = User(name="Store1Manager", email="store1manager@example.com", password="1234")
        db.session.add(user1)
        db.session.commit()
        # group = Group(id=1, name="storeowner")
        # user.groups = [group]
        # db.session.add(group)
        # db.session.commit()
        # role = Role(name="owner")
        # user.roles = [role]
        # db.session.add(role)
        # db.session.commit()
        # role1 = Role(
        #     name="reader",
        #     restrictions=dict(
        #         stores=['create', 'update', 'delete'],
        #     )
        # )
        # user1.roles = [role1]
        # db.session.add(role1)
        # db.session.commit()


    from authlogin.resources.user import UserRegister, UserLogin, UserLogout
    from main.resources.store import NewStore, Store, StoreList


    api.add_resource(UserRegister, "/register")
    api.add_resource(UserLogin, "/login")
    api.add_resource(UserLogout, "/logout")


    api.add_resource(NewStore, "/store")
    api.add_resource(Store, "/store/<int:_id>")
    api.add_resource(StoreList, "/stores")
    app.run(port=5000, debug=True)