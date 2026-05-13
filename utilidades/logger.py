# Importamos fecha y hora del sistema
from datetime import datetime


# Función para registrar eventos y errores
def registrar_log(mensaje):

    # Abrimos el archivo logs.txt
    with open("logs.txt", "a", encoding="utf-8") as archivo:

        # Registramos fecha y mensaje
        archivo.write(f"[{datetime.now()}] {mensaje}\n")