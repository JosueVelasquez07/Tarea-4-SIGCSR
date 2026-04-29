from .base import entidad   

class Servicio(entidad):
    def __init__(self, id_servicio, nombre, precio):
        self.id_servicio = id_servicio
        self.nombre = nombre
        self.precio = precio

    def mostrar_info(self):
        return f"Servicio: {self.nombre}, Precio: {self.precio}"

    def actualizar_info(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)