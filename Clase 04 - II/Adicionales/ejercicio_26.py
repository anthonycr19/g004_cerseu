"""Funciones"""

"""
Crear una función para filtrar números de una lista a partir de una umbral dada
"""

def filtrar_mayores(lista, umbral):
    unicos = []
    for elemento in lista:
        if elemento > umbral:
            unicos.append(elemento)
    return unicos

numeros = [3, 15, 19, 4, 206, 25, 74, 9]
print(filtrar_mayores(numeros, 25))


#La función de parte inferior se puede reemplazar con la siguiente función
#preservando las buenas prácticas, reemplaza para ver los mismo efectos
"""
def filtrar_mayores(lista, umbral):
    return [elemento for elemento in lista if elemento > umbral]]
"""