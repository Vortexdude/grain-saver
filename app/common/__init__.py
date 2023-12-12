from .settings import Settings
from flask_jwt_extended import JWTManager

_settings = Settings()

jwt = JWTManager()
