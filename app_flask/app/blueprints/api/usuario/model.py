from app.blueprints.api.interfaces import IModel
from app.models.sqlalchemy.usuario_model import UsuarioModel as model_sqlalchemy
from app.models.peewee.usuario_model import UsuarioModel as model_peewee


class UsuarioModel(IModel):

    __slots__ = ("__orm",)

    def __init__(self, orm: str):
        self.__orm = orm
        self._get_model()

    def _get_model(self):

        match self.__orm:
            case "peewee":
                return model_peewee()
            
            case "sqlalchemy":
                return model_sqlalchemy()
            
            case _:
                raise Exception("Não existe um model.")