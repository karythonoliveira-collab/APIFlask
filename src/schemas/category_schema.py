from src.models import CategoriaModel
from src import ma
from marshmallow import fields

class CategoriaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CategoriaModel
        load_instance = True