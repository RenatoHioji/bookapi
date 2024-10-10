from api import ma
from marshmallow import Schema, fields

class BookSchema(ma.Schema):
    class Meta:
        fields = ('_id', 'title', 'sinopse', 'year')
        
    _id = fields.Str()
    title = fields.Str(required=True)
    sinopse = fields.Dict(required=True)
    year = fields.Int(required=True)