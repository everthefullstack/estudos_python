from flask import Flask
from app.models.peewee.usuario_model import UsuarioModel
from app.models.sqlalchemy.base_model import db as sqlalchemy
from app.models.peewee.base_model import db as peewee


class TablesPeewee:
    
    def __create_tables(self):
        try:
            tables = [UsuarioModel,]
            peewee.database.create_tables(tables)

        except Exception as error:
            print(f"Erro ao criar tabela => {error}")
                
    def process(self):
        self.__create_tables()

class TablesSqlalchemy:
    
    def __create_tables(self):
        try:
            sqlalchemy.metadata.create_all()

        except Exception as error:
                print(f"Erro ao criar tabela => {error}")

    def process(self):
        self.__create_tables()

def init_app(app: Flask):

    match app.config.ORM:
        case "peewee":
            TablesPeewee().process()
        
        case "sqlalchemy":
            TablesSqlalchemy().process()

    print(f"Tabelas do orm {app.config.ORM} criadas com sucesso.")
