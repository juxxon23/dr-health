from marshmallow import validate, fields, Schema, validates, ValidationError


class PatientSignin(Schema):

    id_u = fields.Str(required=True, validate=validate.Length(min=6, max=20))
    name = fields.Str(required=True, validate=validate.Length(min=3, max=20))
    last = fields.Str(required=True, validate=validate.Length(min=3, max=20))
    mail = fields.Str(required=True, validate=validate.Length(min=10, max=50))
    phone = fields.Str(required=True, validate=validate.Length(min=7, max=10))
    password = fields.Str(required=True, validate=validate.Length(min=8, max=20))
    age = fields.Int(required=True)
    role = fields.Str(required=True, validate=validate.Equal("2"))
    id_family = fields.Str(required=True, validate=validate.Length(min=1, max=10))
    id_m = fields.Str(required=True, validate=validate.Length(max=10))
