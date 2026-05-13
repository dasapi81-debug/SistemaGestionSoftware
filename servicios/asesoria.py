# Importamos clase Servicio
from modelos.servicio import Servicio


# Clase Asesoria
class Asesoria(Servicio):

    # Método sobrescrito
    def calcular_costo(self, horas):

        return self.tarifa * horas

    # Método sobrescrito
    def descripcion(self):

        return "Servicio de asesorías especializadas"