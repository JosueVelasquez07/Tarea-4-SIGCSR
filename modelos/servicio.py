from abc import abstractmethod
from .base import Entidad

class Servicio(Entidad):

    def __init__(self, id_servicio, nombre, precio):
        self._id_servicio = id_servicio
        self._nombre = nombre
        self._precio = precio

    def mostrar_info(self):
        return f"Servicio: {self._nombre}, Precio base: {self._precio}"

    def actualizar_info(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, f"_{key}"):
                setattr(self, f"_{key}", value)

    @abstractmethod
    def calcular_costo(self, duracion):
        pass

    # Getter recomendado
    def get_nombre(self):
        return self._nombre