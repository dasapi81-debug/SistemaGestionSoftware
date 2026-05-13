# Importamos excepción personalizada
from modelos.excepciones import ReservaError


# Clase Reserva
class Reserva:

    # Constructor
    def __init__(self, cliente, servicio, horas):

        # Atributos
        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas
        self.estado = "Pendiente"

    # Confirmar reserva
    def confirmar(self):

        # Validación
        if self.horas <= 0:

            raise ReservaError(
                "No se puede confirmar una reserva inválida"
            )

        # Cambiar estado
        self.estado = "Confirmada"

    # Cancelar reserva
    def cancelar(self):

        self.estado = "Cancelada"

    # Procesar reserva
    def procesar(self):

        try:

            # Calcular costo
            costo = self.servicio.calcular_costo(
                self.horas
            )

            # Confirmar reserva
            self.confirmar()

            return costo

        # Captura de errores
        except Exception as e:

            # Encadenamiento de excepción
            raise ReservaError(
                "Error procesando la reserva"
            ) from e