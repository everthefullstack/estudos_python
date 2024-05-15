from abc import ABC, abstractmethod


class IDataMapper(ABC):

    @abstractmethod
    def _get_data_mapper(self) -> None:
        pass

class IModel(ABC):

    @abstractmethod
    def _get_model(self) -> None:
        pass

class IBase(ABC):

    @abstractmethod
    def get(self) -> None:
        pass

    @abstractmethod
    def get_all(self) -> None:
        pass

    @abstractmethod
    def create(self) -> None:
        pass
    
    @abstractmethod
    def update(self) -> None:
        pass

    @abstractmethod
    def delete(self) -> None:
        pass

class IOrmDataMapper(IBase):
    pass
    
class IRepository(IBase):
    pass

class IController(IBase):
    pass

class IService(IBase):
    pass