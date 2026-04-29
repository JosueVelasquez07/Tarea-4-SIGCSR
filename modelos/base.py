from abc import ABC, abstractmethod

class Entidad(ABC):

    @abstractmethod
    def mostrar_info(self):
        pass