# Excepción para errores relacionados con clientes
class ClienteError(Exception):
    pass


# Excepción para errores relacionados con servicios
class ServicioError(Exception):
    pass


# Excepción para errores relacionados con reservas
class ReservaError(Exception):
    pass