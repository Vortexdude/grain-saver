from flask.views import MethodView
from flask_smorest import Blueprint
from .schema import EventRegisterSchema, UpdateEventSchema
from .controller import EventController
# /create_event - POST
# /update_event - PUT
# /event_details - GET
# /trigger_event - POST
# /detele_event - DELETE

blp = Blueprint("Event Operations", __name__, description="Organize your events with ")


@blp.route("/event_details")
class GetEvent(MethodView):

    def get(self):
        """Get the events details"""
        return

@blp.route("/create_event")
class CreateEvent(MethodView):

    @blp.arguments(EventRegisterSchema)
    def post(self, event_data):
        """Create Events for the user"""

        return EventController.create_event(event_data)

@blp.route("/update_event")
class UpdateEvent(MethodView):
 
    @blp.arguments(UpdateEventSchema)
    def put(self, id):
        """update the Events"""
        return {"Status": f"Done{id}"}

@blp.route("/delete_event")
class DeleteEvent(MethodView):

    def delete(self):
        """Delete the event"""
        return {"Status": "Done"}
