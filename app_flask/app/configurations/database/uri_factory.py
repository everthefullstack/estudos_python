from app.configurations.database import uris
from inspect import getmembers, isclass, isabstract
from abc import ABC, abstractmethod
from typing import Union


# classe abstrata (interface) contendo os contratos (funções) 
# que as classes herdeiras deverão conter
class IUriFactory(ABC):

    @abstractmethod
    def load_uris(self) -> None:
        pass
    
    @abstractmethod
    def create(self, uri: str) -> Union[uris.Uri, ValueError]:
        pass

# fábrica para retornar objetos derivados da subclasse Uri
class UriFactory(IUriFactory):
    
    uri_implementations = {}

    def __init__(self) -> None:
        self.load_uris()

    # Carrrega as opções de uri na dict uri_implementations
    def load_uris(self) -> None:

        # retorna o nome e o tipo da classe baseado na condição exigida,
        # que são as classes importadas do __init__
        implementations = getmembers(uris, lambda bd: isclass(bd) and not isabstract(bd))

        # se tipo for uma classe e se a subclasse for a classe uri, que é uma
        # herança de implementação da interface IUri, atribui valor a dict de
        # uri_implementations
        for nome, tipo in implementations:
            if isclass(tipo) and issubclass(tipo, uris.Uri):
                self.uri_implementations[nome.upper()] = tipo

    #retorna a classe concreta presente na dict uri_implementations, 
    # que herda da subclasse Uri, que é uma herança de implementação,
    # que herda da interface IUri, baseado no nome passado por parâmetro
    def create(self, uri: str) -> Union[uris.Uri, ValueError]:

        if uri.upper() in self.uri_implementations:
            # os parenteses servem para mandar a classe já instanciada como resposta
            return self.uri_implementations[uri.upper()]
        else:
            raise ValueError(f"{uri} não é suportado nesse app.")