from marshmallow import Schema, fields, validate



class BaseEventSchema(Schema):
    id = fields.Int(dump_only=True)
    event_id = fields.Str(dump_only=True)
    event_name = fields.Str(required=True)
    event_type = fields.Str(required=True)
    event_location = fields.Str(required=True)
    event_date = fields.Str(required=True, validate=validate.Length(max=10))
    event_time = fields.Str(required=True, validate=validate.Length(max=8))
    event_orgnizer = fields.Str(required=True)
    event_orgnizer_id = fields.Str(required=True)

class EventRegisterSchema(BaseEventSchema):
    pass

class UpdateEventSchema(BaseEventSchema):
    event_id = fields.Str(required=True)
    event_name = fields.Str(required=False, missing=None)
    event_type = fields.Str(required=False, missing=None)
    event_location = fields.Str(required=False, missing=None)
    event_date = fields.Str(required=False, validate=validate.Length(max=10), missing=None)
    event_time = fields.Str(required=False, validate=validate.Length(max=8), missing=None)
    event_orgnizer = fields.Str(required=False, missing=None)
    event_orgnizer_id = fields.Str(required=False, missing=None)
