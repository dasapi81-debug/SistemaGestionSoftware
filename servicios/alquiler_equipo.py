# Importamos clase Servicio
from modelos.servicio import Servicio


# Clase AlquilerEquipo
class AlquilerEquipo(Servicio):

    # Método para calcular costo
    def calcular_costo(self, horas, impuesto=0.19):

        subtotal = self.tarifa * horas

        return subtotal + (subtotal * impuesto)

    # Método descripción
    def descripcion(self):

        return "Servicio de alquiler de equipos"

    # Método heredado obligatorio
    def mostrar_informacion(self):

        return (
            f"Servicio: {self.nombre} "
            f"| Tarifa: {self.tarifa}"
        )