from flask import Flask
from flask_restful import Api

import main.controllers.userControllers as uc

from .config import config_by_name


api = Api()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    from main.models import db, bcrypt
    from main.services import jwt
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    api.add_resource(uc.UserRegistration, '/api/register')
    api.add_resource(uc.UserLogin, '/api/login')
    api.add_resource(uc.TutorProfile, '/api/tutor/profile')
    api.add_resource(uc.UserProfile, '/api/user/profile')
    api.init_app(app)

    return app