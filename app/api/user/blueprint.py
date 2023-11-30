from flask.views import MethodView
from flask_smorest import Blueprint
from .schema import UserRegisterSchema, LoginSchema
from .controller import UserController


blp = Blueprint("User Operations", __name__, description="Register, login and get user details")

@blp.route("/register")
class RegisterUser(MethodView):
    @blp.arguments(UserRegisterSchema)
    def post(self, userdata):
        """register User in the database"""

        return UserController.register_user(userdata)

@blp.route("/user/<string:fname>")
class GetUsers(MethodView):
    def get(self, fname):
        """Get user details by their id"""

        return UserController.fetch_user(fname)

@blp.route("/login")
class LoginUser(MethodView):

    @blp.arguments(LoginSchema)
    def post(self, login_details):
        """Authentication using phone and password"""

        return UserController.login(login_details)
