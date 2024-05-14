from flask import request
from app.blueprints.api.interfaces import IController, IService


class UsuarioController(IController):

    __slots__ = ("__service",)

    def __init__(self, service: IService) -> None:
        self.__service = service

    def get(self):
        
        dataset = request.get_json()
        return self.__service.get(dataset)
    
    def get_all(self):
        
        dataset = request.get_json()
        return self.__service.get_all(dataset)
    
    def create(self):
        return False

    def update(self):
        return False

    def delete(self):
        return False