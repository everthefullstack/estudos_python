from flask import Flask
from app.configurations.database import SqliteBase, PostgresqlBase


class Sqlite(SqliteBase):
    def __init__(self, app: Flask) -> None:
         super().__init__(app)
    
    def create_db_connection(self):
        return f"{self._database_uri}{self._database_path}{self._database_name}.db"
  
class Postgresql(PostgresqlBase):
    def __init__(self, app: Flask) -> None:
         super().__init__(app)

    def create_db_connection(self):
        return f"{self._database_uri}{self._database_name}{self._database_options}{self._database_schema}"
    
class Orm:

    def __init__(self, app: Flask) -> None:
        self.app = app
        self._database_env = app.config.ENV

    def process(self):

        match self._database_env:
                case "production":
                    return Postgresql(self.app).create_db_connection()

                case "development":
                    return Sqlite(self.app).create_db_connection()