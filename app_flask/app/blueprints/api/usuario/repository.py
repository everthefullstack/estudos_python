from app.blueprints.api.interfaces import IRepository, IOrmDataMapper


class UsuarioRepository(IRepository):
    
    __slots__ = ("data_mapper",)

    def __init__(self, data_mapper: IOrmDataMapper) -> None:
        self.__data_mapper = data_mapper

    def get(self, id: int):
        return self.__data_mapper.get(id)

    def get_all(self):
        return self.__data_mapper.get_all()
    
    def create(self):
        return False

    def update(self):
        return False

    def delete(self):
        return False