from flask.views import MethodView
from flask_smorest import Blueprint
from .schema import UserRegisterSchema


blp = Blueprint("User Registration", __name__, description="Users Operations")

@blp.route("/register")
class Users(MethodView):
 
    @blp.arguments(UserRegisterSchema)
    def post(self, userdata):
        return {"data": userdata}
