from pathlib import Path
from .database import Database


#classe concreta
class Sqlite(Database):

    def __init__(self) -> None:
        super().__init__()
        self._database_path = Path("arq/database/").absolute().resolve().__str__()

    def get_db_uri(self) -> str:
        return f"{self._database_uri}{self._database_path}{self._database_name}.db"