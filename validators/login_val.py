from marshmallow import fields, Schema, validate, ValidationError

class LoginValidator(Schema):
    mail = fields.String(required=True, validate=validate.Length(min=13, max=50))
    password = fields.String(required=True, validate=validate.Length(min=8, max=20))
