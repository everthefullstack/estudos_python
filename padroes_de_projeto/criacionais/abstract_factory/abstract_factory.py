from abc import ABC, abstractmethod
from peewee import SqliteDatabase, PostgresqlDatabase, MySQLDatabase
from flask import Flask
from pathlib import Path
from typing import Type, Union


"""
FÁBRICAS SÃO SIMPLESMENTE OPERAÇÕES(MÉTODOS OU FUNÇÕES) QUE CRIAM OBJETOS
"""

# classe abstrata(interface) contendo os contratos(funções) que as classes implementadas deverão conter
class OrmInterface(ABC):
    
    @abstractmethod
    def create_db_connector(self) -> None:
        pass

# classe concreta que utiliza o conceito de herança de implementação,
# atuando como classe base, fornecendo implementações comuns que serão
# compartilhadas para todas as subclasses concretas
class OrmBase(OrmInterface):

    def __init__(self, app: Flask) -> None:
        self._database_uri = app.config.DATABASE_URI
        self._database_name = app.config.DATABASE_NAME

#subclasse concreta
class SqlitePeewee(OrmBase):
    
    def __init__(self, app: Flask) -> None:
        super().__init__(app)
        self.__database_path = Path(app.config.DATABASE_PATH).absolute().resolve().__str__()

    def create_db_connector(self):
        return SqliteDatabase(f"{self._database_uri}/{self.__database_path}/{self._database_name}.db", pragmas={'foreign_keys': 1})

#subclasse concreta
class PostgresqlPeewee(OrmBase):
    
    def __init__(self, app: Flask) -> None:
        super().__init__(app)
        self.__database_schema = app.config.DATABASE_SCHEMA
        self.__database_options = app.config.DATABASE_OPTIONS

    def create_db_connector(self):
        return PostgresqlDatabase(f"""{self._database_uri}
                                      {self._database_name}
                                      {self.__database_options}
                                      {self.__database_schema}""", 
                                       autocommit=True, 
                                       autoconnect=True, 
                                       autorollback=True)

#subclasse concreta  
class MySqlPeewee(OrmBase):
    
    def __init__(self, app: Flask) -> None:
        super().__init__(app)

    def db_connector(self):
        return MySQLDatabase(f"{self._database_uri}{self._database_name}")

#fábrica para retornar objetos derivados da classe OrmBase, que tem contratos de OrmInterface
class OrmFactoy:

    def __init__(self, orm_connector: Type[OrmInterface]) -> None:
        self.__orm_connector = orm_connector

    def create_connector(self) -> Union[object, Exception]:
        
        try:
            return self.__orm_connector()
        
        except Exception as error:
            return error
        
orm = OrmFactoy(SqlitePeewee)
print(orm)