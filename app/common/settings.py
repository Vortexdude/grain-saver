import os
from dotenv import load_dotenv

class Settings:

    def __init__(self):
        load_dotenv(verbose=True)

    @staticmethod
    def _get_env(key, default):
        return os.getenv(key, default)

    @property
    def api_title(self):
        self._get_env('API_TITLE', "Grain Saver API")

    @property
    def web_app_name(self):
        self._get_env('WEB_APP_NAME', "Grain Saver")

    @property
    def host(self):
        self._get_env('HOST', "0.0.0.0")

    @property
    def web_port(self):
        self._get_env('WEB_PORT', 5000)

    @property
    def api_version(self):
        self._get_env('API_VERSION', "1.0")

    @property
    def openapi_version(self):
        self._get_env('OPENAPI_VERSION', "3.0.3")

    @property
    def openapi_url_prefix(self):
        self._get_env('OPENAPI_URL_PREFIX', "/")

    @property
    def openapi_swagger_ui_path(self):
        self._get_env('OPENAPI_SWAGGER_UI_PATH', "/swagger-ui")

    @property
    def openapi_swagger_ui_url(self):
        self._get_env('OPENAPI_SWAGGER_UI_URL', "https://cdn.jsdelivr.net/npm/swagger-ui-dist/")
