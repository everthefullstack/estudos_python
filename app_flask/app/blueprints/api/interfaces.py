from abc import ABC, abstractmethod
from typing import Union, List


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
    def get(self, id: int) -> Union[List[dict], Exception]:
        pass

    @abstractmethod
    def get_all(self) -> Union[List[dict], Exception]:
        pass

    @abstractmethod
    def create(self, dataset: dict) -> Union[int, Exception]:
        pass
    
    @abstractmethod
    def update(self, dataset: dict) -> Union[int, Exception]:
        pass

    @abstractmethod
    def delete(self, id: int) -> Union[True, Exception]:
        pass

class IOrmDataMapper(IBase):
    pass
    
class IRepository(IBase):
    pass

class IController(IBase):
    pass

class IService(IBase):
    pass