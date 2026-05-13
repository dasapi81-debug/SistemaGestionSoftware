# Importamos clase Servicio
from modelos.servicio import Servicio

# Importamos excepción personalizada
from modelos.excepciones import ServicioError


# Clase ReservaSala
class ReservaSala(Servicio):

    # Método para calcular costo
    def calcular_costo(self, horas, descuento=0):

        # Validación
        if horas <= 0:

            raise ServicioError(
                "Las horas deben ser mayores a cero"
            )

        # Calcular total
        total = self.tarifa * horas

        # Aplicar descuento
        total -= total * descuento

        return total

    # Método descripción
    def descripcion(self):

        return "Servicio de reserva de salas"

    # Método heredado obligatorio
    def mostrar_informacion(self):

        return (
            f"Servicio: {self.nombre} "
            f"| Tarifa: {self.tarifa}"
        )