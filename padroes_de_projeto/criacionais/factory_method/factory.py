import databases
from inspect import getmembers, isclass, isabstract
from abc import ABC, abstractmethod
from typing import Union


# classe abstrata (interface) contendo os contratos (funções) 
# que as classes herdeiras deverão conter
class IDatabaseFactory(ABC):

    @abstractmethod
    def load_databases(self):
        ...
    
    @abstractmethod
    def process(self):
        ...

# fábrica para retornar objetos derivados da subclasse Database
class DatabaseFactory(IDatabaseFactory):
    
    database_implementations = {}

    def __init__(self) -> None:
        self.load_databases()

    # Carrrega as opções de database na dict database_implementations
    def load_databases(self) -> None:

        # retorna o nome e o tipo da classe baseado na condição exigida,
        # que são as classes importadas do __init__
        implementations = getmembers(databases, lambda bd: isclass(bd) and not isabstract(bd))

        # se tipo for uma classe e se a subclasse for a classe database, que é uma
        # herança de implementação da interface IDatabase, atribui valor a dict de
        # database_implementations
        for nome, tipo in implementations:
            if isclass(tipo) and issubclass(tipo, databases.Database):
                self.database_implementations[nome.upper()] = tipo

    #retorna a classe concreta presente na dict database_implementations, 
    # que herda da subclasse Database, que é uma herança de implementação,
    # que herda da interface IDatabase, baseado no nome passado por parâmetro
    def process(self, database: str) -> Union[databases.Database, ValueError]:

        if database.upper() in self.database_implementations:

            # os parenteses servem para mandar a classe já instanciada como resposta
            return self.database_implementations[database.upper()]()
        else:
            raise ValueError(f"{database} não é suportado nesse sistema.")