from flask import Flask
from flask_smorest import Api
from app.api.user import UserBlueprint
from app.api.events import EventBlueprint
from app.config import config_by_name

def create_app(env):
    app = Flask(__name__)
    app.config.from_object(config_by_name[env])
    api = Api(app)
    api.register_blueprint(UserBlueprint)
    api.register_blueprint(EventBlueprint)
    return app

def register_blueprint(app):
    global api 
    api.register_blueprint(UserBlueprint)
    api.register_blueprint(EventBlueprint)
