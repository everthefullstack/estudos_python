from flask import Flask
from playhouse.postgres_ext import PostgresqlExtDatabase, SqliteDatabase
from app.models.peewee.base_model import BaseModel
from app.configurations.database import AbcDatabase


class Peewee(AbcDatabase):

    __slots__ = ("__database_env", "__database_options")
    
    def __init__(self, app: Flask) -> None:
        super().__init__(app)
        self.__database_env = app.config.ENV
        self.__database_options = app.config.DATABASE_OPTIONS

    def __config_db_connection(self):
        match self.__database_env:
            case "production":
                BaseModel._meta.database.initialize(PostgresqlExtDatabase(f"""{self._database_uri}
                                                              {self._database_name}
                                                              {self.__database_options}
                                                              {self._database_schema}""", 
                                                               autocommit=True, 
                                                               autoconnect=True, 
                                                               autorollback=True))

            case "development":
                BaseModel._meta.database.initialize(SqliteDatabase(f"{self._database_path}/{self._database_name}.db", pragmas={'foreign_keys': 1}))
                
    def init_app(self):
        self.__config_db_connection()

def init_app(app: Flask) -> None:
    Peewee(app).init_app()