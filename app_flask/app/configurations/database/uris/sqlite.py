from app.configurations.database.uris.uris import SqliteBase
from flask import Flask


class Sqlite(SqliteBase):
    def __init__(self, app: Flask) -> None:
         super().__init__(app)
    
    def get_uri(self) -> str:
        return f"{self._database_uri}{self._database_path}{self._database_name}.db"