from flask import Flask
from flask_smorest import Api
from app.api.user import UserBlueprint
from app.config import config_by_name

def create_app(env):
    app = Flask(__name__)
    # app.config.from_object(config_by_name[env])
    app.config['PROPAGATE_EXCEPTIONS'] = "True"
    app.config['API_TITLE'] = "Grain Saver API"
    app.config['WEB_APP_NAME'] = "Grain Saver"
    app.config['HOST']="0.0.0.0"
    app.config['WEB_PORT']=5000
    app.config['API_VERSION']="2.5"
    app.config['OPENAPI_VERSION']="3.0.3"
    app.config['OPENAPI_URL_PREFIX']="/"
    app.config['OPENAPI_SWAGGER_UI_PATH']="/swagger-ui"
    app.config['OPENAPI_SWAGGER_UI_URL']="https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    api = Api(app)
    api.register_blueprint(UserBlueprint)
    return app
