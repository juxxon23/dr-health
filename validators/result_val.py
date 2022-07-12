from marshmallow import  validate, fields, Schema

class ResultVal(Schema):
    id_r = fields.Str(required=True, validator=validate.Length(max=10))
    id_o = fields.Str(required=True, validator=validate.Length(max=10))
    file_r = fields.Raw(requered=True)
