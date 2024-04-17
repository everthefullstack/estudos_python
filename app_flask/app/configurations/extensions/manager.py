from dynaconf import FlaskDynaconf
from flask import Flask


def init_app(app: Flask) -> None:
    FlaskDynaconf(app)