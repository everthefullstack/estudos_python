from abc import ABC, abstractmethod
from flask import Flask


class SettingsInterface(ABC):
    
    @abstractmethod
    def _get_cursor_sql_postgres(self) -> None:
        pass

    @abstractmethod
    def _create_database_postgres(self) -> None:
        pass

    @abstractmethod
    def _create_schema_postgres(self) -> None:
        pass

    @abstractmethod
    def _create_postgres(self) -> None:
        pass

    @abstractmethod
    def _create_dir_sqlite(self) -> None:
        pass

    @abstractmethod
    def _create_database_sqlite(self) -> None:
        pass

    @abstractmethod
    def _create_sqlite(self) -> None:
        pass

    @abstractmethod
    def _config_database(self) -> None:
        pass

# classe que utiliza o conceito de herança de implementação,
# atuando como classe base, fornecendo implementações comuns que serão
# compartilhadas para todas as subclasses concretas
class SettingsBase(SettingsInterface):
    __slots__ = ("_database_uri", "_database_name", 
                 "_database_schema", "_database_path")
    
    def __init__(self, app: Flask) -> None:
        self._database_uri = app.config.DATABASE_URI
        self._database_name = app.config.DATABASE_NAME
        self._database_schema = app.config.DATABASE_SCHEMA
        self._database_path = app.config.DATABASE_PATH

# classe abstrata(interface) contendo os contratos(funções) que as classes implementadas deverão conter
class ConnectionInterface(ABC):

    @abstractmethod
    def create_db_connection(self) -> None:
        pass

# classes que utilizam o conceito de herança de implementação,
# atuando como classe base, fornecendo implementações comuns que serão
# compartilhadas para todas as subclasses concretas
class ConnectionBase(ConnectionInterface):
    __slots__ = ("_database_uri", "_database_name",)
    
    def __init__(self, app: Flask) -> None:
        self._database_uri = app.config.DATABASE_URI
        self._database_name = app.config.DATABASE_NAME

class SqliteBase(ConnectionBase):
    
    __slots__ = ("_database_path")
    
    def __init__(self, app: Flask) -> None:
        super().__init__(app)
        self._database_path = app.config.DATABASE_PATH

class PostgresqlBase(ConnectionBase):
    
    __slots__ = ("__database_schema", "__database_options")

    def __init__(self, app: Flask) -> None:
        super().__init__(app)
        self._database_schema = app.config.DATABASE_SCHEMA
        self._database_options = app.config.DATABASE_OPTIONS