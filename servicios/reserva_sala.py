# Importamos clase Servicio
from modelos.servicio import Servicio

# Importamos excepción personalizada
from modelos.excepciones import ServicioError


# Clase ReservaSala
class ReservaSala(Servicio):

    # Método sobrescrito
    def calcular_costo(self, horas, descuento=0):

        # Validación
        if horas <= 0:

            raise ServicioError(
                "Las horas deben ser mayores a cero"
            )

        # Cálculo total
        total = self.tarifa * horas

        # Aplicar descuento
        total -= total * descuento

        return total

    # Método sobrescrito
    def descripcion(self):

        return "Servicio de reserva de salas"