"""Manejo de errores"""
"""
Crear nueva expeción en un except

validar_usuario
"""

def validar_usuario(usuario):
    try:
        if not usuario:
            raise ValueError("El nombre del usuario no debería estar vacío")
        if len(usuario) < 3:
            raise ValueError("El nombre de usuario debe tener al menos 3 caracteres")
        return "Usuario {} válido".format(usuario)
    except ValueError as error:
        print("Error de validacion: {}".format(error))
        # Se lanza para que el error se maneje a otro nivel
        raise

try:
    validar_usuario("")
except ValueError as error:
    print("Se capturó afuera: {}".format(error))

try:
    validar_usuario("Me")
except ValueError as error:
    print("Se capturó afuera: {}".format(error))
