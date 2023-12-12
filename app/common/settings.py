import os
from dotenv import load_dotenv

class Settings:

    def __init__(self):
        load_dotenv(verbose=True)

    @staticmethod
    def _get_env(key: str, default):
        return os.getenv(key, default)

    @property
    def jwt_secret_key(self) -> str:
        return self._get_env("JWT_SECRET_KEY", "secret")

    @property
    def api_title(self) -> str:
        return self._get_env('API_TITLE', "Grain Saver API")

    @property
    def web_app_name(self):
        return self._get_env('WEB_APP_NAME', "Grain Saver")

    @property
    def host(self):
        return self._get_env('HOST', "0.0.0.0")

    @property
    def web_port(self):
        return self._get_env('WEB_PORT', 5000)

    @property
    def api_version(self):
        return self._get_env('API_VERSION', "1.0")

    @property
    def openapi_version(self):
        return self._get_env('OPENAPI_VERSION', "3.0.3")

    @property
    def openapi_url_prefix(self):
        return self._get_env('OPENAPI_URL_PREFIX', "/")

    @property
    def openapi_swagger_ui_path(self):
        return self._get_env('OPENAPI_SWAGGER_UI_PATH', "/swagger-ui")

    @property
    def openapi_swagger_ui_url(self):
        return self._get_env('OPENAPI_SWAGGER_UI_URL', "https://cdn.jsdelivr.net/npm/swagger-ui-dist/")

    @property
    def jwt_blacklist_enabled(self) -> bool:
        return self._get_env("JWT_BLACKLIST_ENABLED", True)
    
    @property
    def jwt_blacklist_tokens(self) -> bool:
        return self._get_env("JWT_BLACKLIST_TOKEN_CHECKS", True)

    @property
    def api_spec_option(self):
        data = {}
        data['security'] = [{"bearerAuth": []}]
        data['components'] = {
                "securitySchemes":
                    {
                        "bearerAuth": {
                            "type":"http",
                            "scheme": "bearer",
                            "bearerFormat": "JWT"
                        }
                    }
            }
        return data