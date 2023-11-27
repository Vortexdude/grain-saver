from flask.views import MethodView
from flask_smorest import Blueprint

# /create_event - POST
# /update_event - PUT
# /event_details - GET
# /trigger_event - POST
# /detele_event - DELETE

blp = Blueprint("Event Operations", __name__, description="Orgnise your events with ")

@blp.route("/create_event")
class CreateEvent(MethodView):
 
    def post(self):
        return {"data": "Created !"}

@blp.route("/update_event")
class UpdateEvent(MethodView):
 
    def put(self):
        return {"Status": "Done"}

@blp.route("/delete_event")
class DeleteEvent(MethodView):

    def delete(self):
        return {"Status": "Done"}
