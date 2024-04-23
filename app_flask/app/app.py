from flask import Flask
from app import configurations
from app.configurations.extensions import manager
from app.operations import tables


def create_app() -> Flask:

    app = Flask(__name__)
    manager.init_app(app)
    configurations.init_app(app)
    tables.init_app(app)
    
    return app