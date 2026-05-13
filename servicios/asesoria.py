# Importamos clase Servicio
from modelos.servicio import Servicio


# Clase Asesoria
class Asesoria(Servicio):

    # Método calcular costo
    def calcular_costo(self, horas):

        return self.tarifa * horas

    # Método descripción
    def descripcion(self):

        return "Servicio de asesorías especializadas"

    # Método heredado obligatorio
    def mostrar_informacion(self):

        return (
            f"Servicio: {self.nombre} "
            f"| Tarifa: {self.tarifa}"
        )