from marshmallow import validate, fields, Schema, validates, ValidationError

class DoctorSignin(Schema):

    id_u = fields.Str(required=True, validate=validate.Length(min = 8, max=20))
    name = fields.Str(required=True, validate=validate.Length(min = 3, max = 20))
    last = fields.Str(required=True, validate=validate.Length(min = 3, max = 20))
    mail = fields.Str(required=True, validate=validate.Length(min = 13, max = 50))
    specialty = fields.Str(required=True, validate= validate.Length(min = 5, max = 50))
    phone = fields.Str(required=True, validate=validate.Length(min = 7, max = 10))
    password = fields.Str(required=True, validate=validate.Length(min=8, max=20))
    role = fields.Str(required=True, validate=validate.Equal("1"))
