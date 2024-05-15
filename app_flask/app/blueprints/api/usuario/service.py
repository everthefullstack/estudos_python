from app.blueprints.api.interfaces import IService, IRepository


class UsuarioService(IService):

    __slots__ = ("__repository",)

    def __init__(self, repository: IRepository) -> None:
        self.__repository = repository

    def get(self, dataset: dict):
        
        try:
            res = self.__repository.get(dataset["id"])
            return res

        except Exception as error:
            return error
    
    def get_all(self):
        
        try:
            res = self.__repository.get_all()
            return res

        except Exception as error:
            return error
    
    def create(self):
        return False

    def update(self):
        return False

    def delete(self):
        return False