from marshmallow import Schema, fields

class UserRegisterSchema(Schema):
    id = fields.Int(dump_only=True)
    fname = fields.Str(required=True)
    lname = fields.Str(required=True)
    location = fields.Str(required=True)
    password = fields.Str(required=True)
    phone = fields.Str(required=True)
