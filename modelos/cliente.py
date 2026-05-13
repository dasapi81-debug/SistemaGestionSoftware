# Importamos clase abstracta Entidad
from modelos.entidad import Entidad

# Importamos excepción personalizada
from modelos.excepciones import ClienteError


# Clase Cliente
class Cliente(Entidad):

    # Constructor de la clase
    def __init__(self, nombre, cedula, correo):

        # Encapsulamiento de atributos
        self.__nombre = nombre
        self.__cedula = cedula
        self.__correo = correo

        # Validamos los datos
        self.validar_datos()

    # Método para validar datos
    def validar_datos(self):

        # Validar nombre vacío
        if not self.__nombre.strip():

            raise ClienteError(
                "El nombre no puede estar vacío"
            )

        # Validar cédula numérica
        if not self.__cedula.isdigit():

            raise ClienteError(
                "La cédula debe contener solo números"
            )

        # Validar longitud de cédula
        if len(self.__cedula) < 7 or len(self.__cedula) > 10:

            raise ClienteError(
                "La cédula debe tener entre 7 y 10 dígitos"
            )

        # Validar correo electrónico
        if "@" not in self.__correo:

            raise ClienteError(
                "Correo electrónico inválido"
            )

    # Método heredado obligatorio
    def mostrar_informacion(self):

        return (
            f"Cliente: {self.__nombre} "
            f"| CC: {self.__cedula}"
        )

    # Getter del nombre
    @property
    def nombre(self):
        return self.__nombre