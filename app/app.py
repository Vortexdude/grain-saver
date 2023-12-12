from flask import Flask
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from app.api.user import UserBlueprint
from app.api.events import EventBlueprint
from app.config import config_by_name
from app.database.db import db

def create_app(env):
    app = Flask(__name__)
    app.config.from_object(config_by_name[env])
    register_extension(app)
    register_blueprint(app)
    return app

def register_extension(app):
    """Extension Registration"""

    global api
    api = Api(app)
    JWTManager(api)
    db.init_app(app)
    with app.app_context():
        db.create_all()

def register_blueprint(app):
    """Blueprint registration"""

    api.register_blueprint(UserBlueprint)
    api.register_blueprint(EventBlueprint)
