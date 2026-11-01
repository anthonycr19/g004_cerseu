"""Manejo de errores"""
"""
    Crear nueva exepción en un except
"""

def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
        raise ValueError(f"No se puede dividir entre {a} y {b}")

try:
    dividir(18, 0)
except ValueError as error:
    print("Error captura afuera: {}".format(error))
