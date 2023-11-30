from marshmallow import Schema, fields

class LoginSchema(Schema):
    phone = fields.Str(required=True)
    password = fields.Str(required=True)

class UserRegisterSchema(LoginSchema):
    id = fields.Int(dump_only=True)
    user_id = fields.Str(dump_only=True)
    fname = fields.Str(required=True)
    lname = fields.Str(required=True)
    location = fields.Str(required=True)
