from flask.views import MethodView
from flask_smorest import Blueprint
from .schema import UserRegisterSchema


blp = Blueprint("User Operations", __name__, description="Register, login and get user details")

@blp.route("/register")
class RegisterUser(MethodView):
 
    @blp.arguments(UserRegisterSchema)
    def post(self, userdata):
        return {"data": userdata}

@blp.route("/user")
class GetUsers(MethodView):
 
    def get(self):
        return {"data": "Success!"}

@blp.route("/login")
class LoginUser(MethodView):

    def post(self):
        return {"data": "login Sucess!"}
