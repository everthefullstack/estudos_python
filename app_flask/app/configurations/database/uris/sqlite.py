from app.configurations.database.uris.uris import SqliteBase
from flask import Flask
from pathlib import Path


class Sqlite(SqliteBase):
    def __init__(self, app: Flask) -> None:
         super().__init__(app)
    
    def get_uri(self) -> str:
        return f"{self._database_uri}" + Path(f"{self._database_path}{self._database_name}.db").absolute().resolve().__str__()
        #return f"{self._database_uri}{self._database_path}{self._database_name}.db"