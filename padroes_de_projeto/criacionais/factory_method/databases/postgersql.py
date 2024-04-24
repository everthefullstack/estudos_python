from .database import Database


#classe concreta
class Postgresql(Database):

    def __init__(self) -> None:
        super().__init__()
        self._database_schema = "factory_method"
        self._database_options = "?options=--search_path%3"

    def get_db_uri(self) -> str:
        return f"{self._database_uri}{self._database_name}{self._database_options}{self._database_schema}"