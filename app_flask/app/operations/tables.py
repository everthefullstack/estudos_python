from flask import Flask
from app.models.peewee.base_model import db as peewee
from app.models.sqlalchemy.base_model import db as sqlalchemy
from app.models.peewee.usuario_model import UsuarioModel as UsuarioPeewee


class TablesPeewee:
    
    def __init__(self, orm: str) -> None:
        self.__orm = orm
        self.__create_tables()

    def __create_tables(self):
        try:
            lista_tables = [UsuarioPeewee,]
            peewee.database.create_tables(lista_tables)

            print(f"Tabelas do orm {self.__orm} criadas com sucesso.")

        except Exception as error:
            print(f"Erro ao criar tabela => {error}")
        
class TablesSqlalchemy:
        
    def __init__(self, orm: str) -> None:
        self.__orm = orm
        self.__create_tables()

    def __create_tables(self):
        try:
            sqlalchemy.create_all()

            print(f"Tabelas do orm {self.__orm} criadas com sucesso.")
            
        except Exception as error:
            print(f"Erro ao criar tabela => {error}")

def init_app(app: Flask):
    
    with app.app_context():
        match app.config.ORM:
            case "peewee":
                TablesPeewee(app.config.ORM)
            
            case "sqlalchemy":
                TablesSqlalchemy(app.config.ORM)
