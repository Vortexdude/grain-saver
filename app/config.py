from app.common import settings


class DefaultConfiguration:
    HOST = settings.host
    PORT = settings.web_port
    APP_NAME = settings.web_app_name
    API_TITLE = settings.api_title
    API_VERSION = settings.api_version
    OPENAPI_VERSION = settings.openapi_version
    OPENAPI_URL_PREFIX = settings.openapi_url_prefix
    OPENAPI_SWAGGER_UI_PATH = settings.openapi_swagger_ui_path
    OPENAPI_SWAGGER_UI_URL = settings.openapi_swagger_ui_url

class DevelopmentConfiguration(DefaultConfiguration):
    """For Development Environment"""
    DEBUG = True
    HOST = settings.host

config_by_name = dict(
    dev=DevelopmentConfiguration
)