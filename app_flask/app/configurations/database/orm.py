from flask import Flask
from app.models.peewee.base_model import db as peewee_db
from app.models.sqlalchemy.base_model import db as sqlalchemy_db


def init_app(app: Flask) -> None:

    match app.config.ORM:
        case "peewee":
            peewee_db.init_app(app)

        case "sqlalchemy":
            sqlalchemy_db.init_app(app)
