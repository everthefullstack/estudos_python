from app.configurations.database.uri_factory import UriFactory
from flask import Flask


def init_app(app: Flask) -> None:

    uri_factory = UriFactory().create(app.config.DATABASE_SOLUTION)
    uri = uri_factory(app).get_uri()

    match app.config.ORM:
        case "peewee":
            app.config["DATABASE"] = uri

        case "sqlalchemy":
            app.config["SQLALCHEMY_DATABASE_URI"] = uri
