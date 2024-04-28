from app.configurations.database.uris.uris import PostgresqlBase
from flask import Flask


class Postgresql(PostgresqlBase):
    def __init__(self, app: Flask) -> None:
         super().__init__(app)

    def get_uri(self) -> str:
        return f"{self._database_uri}{self._database_name}{self._database_options}{self._database_schema}"