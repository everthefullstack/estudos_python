from flask import Flask, Blueprint
from app.blueprints.api.usuario.model import UsuarioModel
from app.blueprints.api.usuario.repository import UsuarioRepository
from app.blueprints.api.usuario.service import UsuarioService
from app.blueprints.api.usuario.controller import UsuarioController
from app.blueprints.api.data_mapper import DataMapper


def init_app(app: Flask):
    
    model = UsuarioModel(orm = app.config.ORM)
    data_mapper = DataMapper(orm = app.config.ORM)(model)
    repository = UsuarioRepository(data_mapper = data_mapper)
    service = UsuarioService(repository = repository)
    controller = UsuarioController(service = service)

    bp = Blueprint("usuario", __name__, url_prefix="/api/v1/usuario")
    bp.add_url_rule(rule="/get_usuario", view_func=controller.get_usuario, methods=["GET"])
    bp.add_url_rule(rule="/get_usuarios", view_func=controller.get_usuarios, methods=["GET"])
    
    app.register_blueprint(bp)