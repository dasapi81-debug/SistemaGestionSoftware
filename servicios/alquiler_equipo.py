# Importamos clase Servicio
from modelos.servicio import Servicio


# Clase AlquilerEquipo
class AlquilerEquipo(Servicio):

    # Método sobrescrito
    def calcular_costo(self, horas, impuesto=0.19):

        # Calcular subtotal
        subtotal = self.tarifa * horas

        # Retornar total con impuesto
        return subtotal + (subtotal * impuesto)

    # Método sobrescrito
    def descripcion(self):

        return "Servicio de alquiler de equipos"