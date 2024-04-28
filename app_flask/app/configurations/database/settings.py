import psycopg2 as pg
import sqlite3 as sql
import os
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from flask import Flask
from pathlib import Path
from abc import ABC, abstractmethod


class ISettings(ABC):
    
    @abstractmethod
    def _get_cursor_sql_postgres(self) -> None:
        pass

    @abstractmethod
    def _create_database_postgres(self) -> None:
        pass

    @abstractmethod
    def _create_schema_postgres(self) -> None:
        pass

    @abstractmethod
    def _create_postgres(self) -> None:
        pass

    @abstractmethod
    def _create_dir_sqlite(self) -> None:
        pass

    @abstractmethod
    def _create_database_sqlite(self) -> None:
        pass

    @abstractmethod
    def _create_sqlite(self) -> None:
        pass

    @abstractmethod
    def _config_database(self) -> None:
        pass

# classe que utiliza o conceito de herança de implementação,
# atuando como classe base, fornecendo implementações comuns que serão
# compartilhadas para todas as subclasses concretas
class SettingsBase(ISettings):

    __slots__ = ("_database_uri", "_database_name", 
                 "_database_schema", "_database_path")
    
    def __init__(self, app: Flask) -> None:
        self._database_uri = app.config.DATABASE_URI
        self._database_name = app.config.DATABASE_NAME
        self._database_schema = app.config.DATABASE_SCHEMA
        self._database_path = app.config.DATABASE_PATH

class Settings(SettingsBase):

    __slots__ = ("__database_solution",)

    def __init__(self, app: Flask) -> None:
        super().__init__(app)
        self.__database_solution = app.config.DATABASE_SOLUTION

    def _get_cursor_sql_postgres(self):
        conn = pg.connect(self._database_uri)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()
        return cursor
    
    def _create_database_postgres(self):
        try:
            sql = f"CREATE DATABASE {self._database_name}"
            cursor = self._get_cursor_sql_postgres()

            with cursor as curr:
                curr.execute(f"SELECT datname FROM pg_database WHERE datname = '{self._database_name}'")
                result = curr.fetchone()

                if result:
                    print("ja existe o banco de dados e não será criado.")
                
                else:
                    curr.execute(sql)            

        except Exception as error:
            print(str(error))
    
    def _create_schema_postgres(self):
        try:
            sql = f"CREATE SCHEMA IF NOT EXISTS {self._database_schema}"
            cursor = self._get_cursor_sql_postgres()

            with cursor as curr:
                curr.execute(sql)                

        except Exception as error:
            print(str(error))

    def _create_postgres(self):
        self._create_database_postgres()
        self._create_schema_postgres()

    def _create_dir_sqlite(self):
        try:
            if not os.path.isdir(self._database_path):
                os.makedirs(self._database_path)
            else:
                print(f"Já existe o diretório {self._database_path} o mesmo não será criado.")

        except Exception as error:
            print(str(error))

    def _create_database_sqlite(self):
        conn = sql.connect(Path(f"{self._database_path}/{self._database_name}.db").absolute().resolve().__str__())
        conn.commit()
        conn.close()

    def _create_sqlite(self):
        self._create_dir_sqlite()
        self._create_database_sqlite()

    def _config_database(self):
        match self.__database_solution:
            case "postgresql":
                self._create_postgres()

            case "sqlite":
                self._create_sqlite()

            case _:
                return "Não existe nenhuma solução de banco de dados cadastrada no arquivo de settings.toml"

    def init_app(self):
        self._config_database()

def init_app(app: Flask):
    Settings(app).init_app()