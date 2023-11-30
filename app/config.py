from app.common import _settings
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    API_TITLE = _settings.api_title
    HOST = _settings.host
    PORT = _settings.web_port
    APP_NAME = _settings.web_app_name
    API_VERSION = _settings.api_version
    OPENAPI_VERSION = _settings.openapi_version
    OPENAPI_URL_PREFIX = _settings.openapi_url_prefix
    OPENAPI_SWAGGER_UI_PATH = _settings.openapi_swagger_ui_path
    OPENAPI_SWAGGER_UI_URL = _settings.openapi_swagger_ui_url

class DevelopmentConfiguration(Config):
    """For Development Environment"""
    DEBUG = True
    HOST = _settings.host
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_dev.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config_by_name = dict(
    dev=DevelopmentConfiguration
)