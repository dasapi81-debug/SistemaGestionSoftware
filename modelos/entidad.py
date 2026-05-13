# Importamos herramientas para crear clases abstractas
from abc import ABC, abstractmethod


# Clase abstracta principal del sistema
class Entidad(ABC):

    # Método abstracto obligatorio
    @abstractmethod
    def mostrar_informacion(self):
        pass