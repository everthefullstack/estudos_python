from abc import ABC, abstractmethod
from flask import Flask
from pathlib import Path


#Classes abstratas que podem ser usadas nas settings

#Classe que recebe informações do app que são comuns para usar
#usar em banco de dados
class AbcDatabase(ABC):
    __slots__ = ("_database_uri", "_database_name", 
                 "_database_schema", "_database_path")
    
    @abstractmethod
    def __init__(self, app: Flask) -> None:
        self._database_uri = app.config.DATABASE_URI
        self._database_name = app.config.DATABASE_NAME
        self._database_schema = app.config.DATABASE_SCHEMA
        self._database_path = Path(app.config.DATABASE_PATH).absolute().resolve().__str__()