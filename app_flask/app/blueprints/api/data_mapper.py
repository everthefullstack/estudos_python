from app.blueprints.api.interfaces import IDataMapper, IOrmDataMapper
from app.models.peewee.base_model import BaseModel as BaseModelPeewee
from app.models.sqlalchemy.base_model import BaseModel as BaseModelSqlalquemy
from typing import Union, List


class PeeweeDataMapper(IOrmDataMapper):

    __slots__ = ("__model",)
    
    def __init__(self, model: BaseModelPeewee):
        self.__model = model
    
    def get(self, id: int) -> Union[List[dict], Exception]:
        try:
            query = (self.__model.select().where(self.__model.id == id))
            return list(query.dicts())

        except Exception as error:
            return error
    
    def get_all(self) -> Union[List[dict], Exception]:
        try:
            query = (self.__model.select())
            return list(query.dicts())

        except Exception as error:
            return error
    
    def create(self):
        return None
    
    def update(self):
        return None
    
    def delete(self):
        return None

class SqlalchemyDataMapper(IOrmDataMapper):

    __slots__ = ("__model",)
    
    def __init__(self, model: BaseModelSqlalquemy):
        self.__model = model

    def get(self, id: int) -> Union[List[dict], Exception]:
        try:
            query = (self.__model.query.filter_by(id = id).all())
            lista_query = [{col.name: getattr(q, col.name) for col in q.__table__.columns} for q in query]
            return lista_query

        except Exception as error:
            return error
    
    def get_all(self) -> Union[List[dict], Exception]:
        try:
            query = (self.__model.query.all())
            lista_query = [{col.name: getattr(q, col.name) for col in q.__table__.columns} for q in query]
            return lista_query
        
        except Exception as error:
            return error
    
    def create(self):
        return None
    
    def update(self):
        return None
    
    def delete(self):
        return None

class DataMapper(IDataMapper):

    __slots__ = ("__orm", "__model")

    def __init__(self, orm: str, model: Union[BaseModelPeewee, BaseModelSqlalquemy]) -> None:
        self.__orm = orm
        self.__model = model
        self._get_data_mapper()

    def _get_data_mapper(self) -> Union[BaseModelPeewee, BaseModelSqlalquemy, Exception]:

        match self.__orm:
            case "peewee":
                return PeeweeDataMapper(self.__model)
            
            case "sqlalchemy":
                return SqlalchemyDataMapper(self.__model)
            
            case _:
                raise Exception("Não existe um data mapper.")