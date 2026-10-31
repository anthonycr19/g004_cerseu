"""Funciones"""

"""
Crear una función para palabras únicas en una frase. Recibirá una frase
y devolverá una lista ordenad alfabéticamente con las palabrás únicas sin 
repetir, ignorando las mayúsuclas y minúsuclas
"""

def palabras_unicas(frase):
    palabras = []
    for palabra in frase.split():
        palabras.append(palabra.lower())
    return sorted(set(palabras))

#sorted(): Ordena los elementos de menor a mayor
#sorted(palabras, reverse=True): Ordena los elementos de mayor a menor
#sorted(palabras, key=len): Ordena los elementos de mayor a menor
#set(): Saca los elementos repetidos de una lista

frase_1 = "Análisis de datos con Python y análisis con Pandas"
print(palabras_unicas(frase_1))

frase_2 = "Entrenamiento de modelo inteligentes de librerías con Python"
print(palabras_unicas(frase_2))