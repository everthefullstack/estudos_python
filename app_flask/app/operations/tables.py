from flask import Flask
from app.models.peewee.base_model import db as peewee
from app.models.sqlalchemy.base_model import db as sqlalchemy
from app.models.peewee.usuario_model import UsuarioModel as UsuarioPeewee


class TablesPeewee:
    
    def __init__(self, orm: str) -> None:
        self._orm = orm

    def __create_tables(self):
        try:
            lista_tables = [UsuarioPeewee,]
            peewee.database.create_tables(lista_tables)

            print(f"Tabelas do orm {self._orm} criadas com sucesso.")

        except Exception as error:
            print(f"Erro ao criar tabela => {error}")
                
    def process(self):
        self.__create_tables()
        
class TablesSqlalchemy:
        
    def __init__(self, orm: str) -> None:
        self._orm = orm

    def __create_tables(self):
        try:
            sqlalchemy.create_all()

            print(f"Tabelas do orm {self._orm} criadas com sucesso.")
            
        except Exception as error:
            print(f"Erro ao criar tabela => {error}")

    def process(self):
        self.__create_tables()
        
def init_app(app: Flask):
    
    with app.app_context():
        match app.config.ORM:
            case "peewee":
                TablesPeewee(app.config.ORM).process()
            
            case "sqlalchemy":
                TablesSqlalchemy(app.config.ORM).process()
