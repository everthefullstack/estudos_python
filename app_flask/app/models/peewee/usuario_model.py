from app.models.peewee.base_model import BaseModel
from peewee import CharField, AutoField


class UsuarioModel(BaseModel):

    id = AutoField()
    nome = CharField(max_length=50)
    senha = CharField(max_length=200)

    class Meta:
        table_name = "tbusuario"