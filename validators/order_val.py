from marshmallow import  validate, fields, Schema

class OrderVal(Schema):
    id_o = fields.Str(required=True, validator=validate.Length(max=10))
    id_a = fields.Str(required=True, validator=validate.Length(max=10))
    diagnosis = fields.Str(required=True, validator=validate.Length(min=2, max=250))
