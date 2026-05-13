# Importamos herramientas para clases abstractas
from abc import ABC, abstractmethod

# Importamos clase base
from modelos.entidad import Entidad


# Clase abstracta Servicio
class Servicio(Entidad, ABC):

    # Constructor
    def __init__(self, nombre, tarifa):

        # Atributos públicos
        self.nombre = nombre
        self.tarifa = tarifa

    # Método abstracto para calcular costo
    @abstractmethod
    def calcular_costo(self, horas):
        pass

    # Método abstracto descripción
    @abstractmethod
    def descripcion(self):
        pass