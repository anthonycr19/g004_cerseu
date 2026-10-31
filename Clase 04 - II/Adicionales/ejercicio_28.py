"""Funciones"""

"""
Crear una función para actualizar notas si existe
Recibirá:
- Una lista de notas (enteros o flotantes)
- La nota que desea reemplazar
- Nueva nota
"""

def actualiza_nota(notas, antigua_nota, nueva_nota):
    if antigua_nota in notas:
        i = notas.index(antigua_nota)  #encuentra el índice en donde está en la lista
        notas[i] = nueva_nota
    return notas

notas = [14, 2, 10, 17, 18, 19, 20]
print(actualiza_nota(notas, 18, 14))
print(actualiza_nota(notas, 8, 4)) # sin cambios

# Variación de la solución de la función solcitada
"""
def actualiza_nota(notas, antigua_nota, nueva_nota):
    for i, nota in enumerate(notas):
        if nota == antigua_nota,:
            notas[i] = nueva_nota
            break
        return notas
        
notas = [14, 2, 10, 17, 18, 19, 20]
print(actualiza_nota(notas, 18, 14))
print(actualiza_nota(notas, 8, 4)) # sin cambios
"""
