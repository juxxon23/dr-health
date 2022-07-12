from marshmallow import  validate, fields, Schema

class AuthorizationVal(Schema):
    id_auth = fields.Str(required=True, validator=validate.Length(max=10))
    id_o = fields.Str(required=True, validator=validate.Length(max=10))
    file_a = fields.Raw(required=True)
