from .model import Events

class EventController:

    @staticmethod
    def create_event(event_data):
        # orgnizer = event_data['event_orgnizer']
        # event = Events.find_byt_filter(event_orgnizer=orgnizer)
        event = Events(**event_data)
        if event:
            return {"Status": "Data Inserted Succesfully!"}
        else:
            return {"Status": "problem with the query"}
