from abc import ABC, abstractmethod


# classe abstrata (interface) contendo os contratos (funções) 
# que as classes herdeiras deverão conter
class IDatabase(ABC):
    
    @abstractmethod
    def get_db_uri(self) -> None:
        pass

# subclasse concreta que utiliza o conceito de herança de implementação,
# atuando como classe base, fornecendo implementações comuns que serão
# compartilhadas com todas as classes concretas
class Database(IDatabase):
    
    def __init__(self) -> None:
        self._database_uri = "sqlite://"
        self._database_name = "factory_method"