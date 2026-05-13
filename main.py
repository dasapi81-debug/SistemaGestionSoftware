# ==============================
# IMPORTACIÓN DE CLASES
# ==============================

# Importamos clase Cliente
from modelos.cliente import Cliente

# Importamos clase Reserva
from modelos.reserva import Reserva

# Importamos excepciones personalizadas
from modelos.excepciones import *

# Importamos servicios
from servicios.reserva_sala import ReservaSala
from servicios.alquiler_equipo import AlquilerEquipo
from servicios.asesoria import Asesoria

# Importamos logger
from utilidades.logger import registrar_log


# ==============================
# LISTAS PRINCIPALES DEL SISTEMA
# ==============================

clientes = []
reservas = []


# ==============================
# FUNCIÓN PRINCIPAL
# ==============================

def ejecutar_operaciones():

    # ==============================
    # CREACIÓN DE CLIENTES
    # ==============================

    operaciones_clientes = [

        lambda: Cliente(
            "David",
            "12345678",
            "david@gmail.com"
        ),

        lambda: Cliente(
            "",
            "12345678",
            "correo@gmail.com"
        ),

        lambda: Cliente(
            "Juan",
            "abc",
            "correo@gmail.com"
        ),

        lambda: Cliente(
            "Ana",
            "1234567",
            "ana@gmail.com"
        ),

        lambda: Cliente(
            "Carlos",
            "98765432",
            "carlos@gmail.com"
        )
    ]

    # Procesamiento de clientes
    for operacion in operaciones_clientes:

        try:

            cliente = operacion()

            clientes.append(cliente)

            print(
                f"Cliente registrado: "
                f"{cliente.nombre}"
            )

            registrar_log(
                f"Cliente registrado: "
                f"{cliente.nombre}"
            )

        except ClienteError as e:

            print(f"ERROR CLIENTE: {e}")

            registrar_log(
                f"ERROR CLIENTE: {e}"
            )

    # ==============================
    # CREACIÓN DE SERVICIOS
    # ==============================

    sala = ReservaSala(
        "Sala VIP",
        50000
    )

    equipo = AlquilerEquipo(
        "Portátil Gamer",
        80000
    )

    asesoria = Asesoria(
        "Asesoría Python",
        120000
    )

    # ==============================
    # OPERACIONES DE RESERVAS
    # ==============================

    operaciones_reservas = [

        lambda: Reserva(
            clientes[0],
            sala,
            3
        ),

        lambda: Reserva(
            clientes[0],
            equipo,
            -1
        ),

        lambda: Reserva(
            clientes[1],
            asesoria,
            2
        ),

        lambda: Reserva(
            clientes[0],
            asesoria,
            5
        ),

        lambda: Reserva(
            clientes[0],
            sala,
            0
        )
    ]

    # ==============================
    # PROCESAMIENTO DE RESERVAS
    # ==============================

    for operacion in operaciones_reservas:

        try:

            reserva = operacion()

            costo = reserva.procesar()

            reservas.append(reserva)

            print(
                f"Reserva exitosa | "
                f"Cliente: {reserva.cliente.nombre} | "
                f"Servicio: {reserva.servicio.nombre} | "
                f"Costo: {costo}"
            )

            registrar_log(
                "Reserva procesada correctamente"
            )

        except Exception as e:

            print(f"ERROR RESERVA: {e}")

            registrar_log(
                f"ERROR RESERVA: {e}"
            )

        finally:

            registrar_log(
                "Finalizó una operación de reserva"
            )


# ==============================
# EJECUCIÓN DEL SISTEMA
# ==============================

ejecutar_operaciones()