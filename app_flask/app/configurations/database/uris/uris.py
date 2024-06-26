from abc import ABC, abstractmethod
from flask import Flask


# classe abstrata(interface) contendo os contratos(funções) que as classes implementadas deverão conter
class IUri(ABC):

    @abstractmethod
    def get_uri(self) -> None:
        pass

# classes que utilizam o conceito de herança de implementação,
# atuando como classe base, fornecendo implementações comuns que serão
# compartilhadas para todas as subclasses concretas
class Uri(IUri):
    
    __slots__ = ("_database_uri", "_database_name",)
    
    def __init__(self, app: Flask) -> None:
        self._database_uri = app.config.DATABASE_URI
        self._database_name = app.config.DATABASE_NAME

class SqliteBase(Uri):
    
    __slots__ = ("_database_path")
    
    def __init__(self, app: Flask) -> None:
        super().__init__(app)
        self._database_path = app.config.DATABASE_PATH

class PostgresqlBase(Uri):
    
    __slots__ = ("__database_schema", "__database_options")

    def __init__(self, app: Flask) -> None:
        super().__init__(app)
        self._database_schema = app.config.DATABASE_SCHEMA
        self._database_options = app.config.DATABASE_OPTIONS