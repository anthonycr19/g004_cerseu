"""Manejo de errores"""
"""
    Exepción personalizada
"""
def validar_edad(edad):
    if edad < 0:
        raise ValueError("Edad no valida, tiene que ser mayor que cero")
    print("Edad correcta")
    return True

"""
raise: Va a generar una exepción deliberadamente cuando una regla no se cumple
"""
validar_edad(18)
validar_edad(-5)