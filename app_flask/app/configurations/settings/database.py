import psycopg2 as pg
import sqlite3 as sql
import os
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from flask import Flask
from app.configurations.settings import AbcDatabase


class Database(AbcDatabase):

    __slots__ = ("__database_solution",)

    def __init__(self, app: Flask) -> None:
        super().__init__(app)
        self.__database_solution = app.config.DATABASE_SOLUTION

    def __get_cursor_sql_postgres(self):
        conn = pg.connect(self._database_uri)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()
        return cursor
    
    def __create_database_postgres(self):
        try:
            sql = f"CREATE DATABASE {self._database_name}"
            cursor = self.__get_cursor_sql_postgres()

            with cursor as curr:
                curr.execute(f"SELECT datname FROM pg_database WHERE datname = '{self._database_name}'")
                result = curr.fetchone()

                if result:
                    print("ja existe o banco de dados e não será criado.")
                
                else:
                    curr.execute(sql)            

        except Exception as error:
            print(str(error))
    
    def __create_schema_postgres(self):
        try:
            sql = f"CREATE SCHEMA IF NOT EXISTS {self._database_schema}"
            cursor = self.__get_cursor_sql_postgres()

            with cursor as curr:
                curr.execute(sql)                

        except Exception as error:
            print(str(error))

    def __create_postgres(self):
        self.__create_database_postgres()
        self.__create_schema_postgres()

    def __create_dir_sqlite(self):
        try:
            if not os.path.isdir(self._database_path):
                os.makedirs(self._database_path)
            else:
                print(f"Já existe o diretório {self._database_path}, o mesmo não será criado.")

        except Exception as error:
            print(str(error))

    def __create_database_sqlite(self):
        conn = sql.connect(f"{self._database_path}/{self._database_name}.db")
        conn.commit()
        conn.close()

    def __create_sqlite(self):
        self.__create_dir_sqlite()
        self.__create_database_sqlite()

    def __config_database(self):
        match self.__database_solution:
            case "postgresql":
                self.__create_postgres()

            case "sqlite3":
                self.__create_sqlite()

            case _:
                return "Não existe nenhuma solução de banco de dados cadastrada no arquivo de settings.toml"

    def init_app(self):
        self.__config_database()

def init_app(app: Flask):
    Database(app).init_app()