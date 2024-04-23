from flask import Flask
from app.configurations.database.orm import Orm
from app.models.peewee.base_model import db as peewee
from app.models.sqlalchemy.base_model import db as sqlalchemy


def init_app(app: Flask) -> None:

    uri = Orm(app).process()

    match app.config.ORM:
        case "peewee":
            app.config["DATABASE"] = uri
            peewee.init_app(app)

        case "sqlalchemy":
            app.config["SQLALCHEMY_DATABASE_URI"] = uri
            sqlalchemy.init_app(app)