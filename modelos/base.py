from abc import ABC, abstractmethod

class entidad(ABC):

    @abstractmethod
    def mostrar_info(self):
        pass
    
    @abstractmethod
    def actualizar_info(self, **kwargs):
        pass