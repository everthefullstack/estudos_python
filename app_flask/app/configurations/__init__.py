from importlib import import_module
from flask import Flask


def init_app(app: Flask) -> None:
    for modules in app.config["CONFIGURATIONS"]:
        for module in app.config[modules]:
            import_module(module).init_app(app)
            print(f"Módulo {module} configurado com sucesso.")
