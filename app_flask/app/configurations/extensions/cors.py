from flask_cors import CORS
from flask import Flask


def init_app(app: Flask) -> None:
    CORS().init_app(app)