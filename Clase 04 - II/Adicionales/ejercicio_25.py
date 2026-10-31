"""Funciones"""

"""
Crear una función llamada eliminar_duplicados(lista) que reciba una lista
de strings y devuelva una nueva lista sin elementos repetidos y manteniendo el 
orden inicial
"""

def eliminar_duplicados(lista):
    vistos = set()  #cojunto vacío
    sin_repetidos = []
    for elemento in lista:
        if elemento not in vistos:  #si el elemento no está en vistos se ejecuta el bloque del if
            vistos.add(elemento)
            sin_repetidos.append(elemento)
    return sin_repetidos


nombres = ["Catherine", "Luis", "Catherine", "Marianela", "Carla", "Luis"]
print(eliminar_duplicados(nombres))

