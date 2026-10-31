"""Funciones"""

"""
Crear una función para actualziar edades actualizar_edades: actualizar_edades(edades, nombre, nueva_edad)
Va a recibir:
- Un diccionario con el nomre y el valor de la edad
- El nombre de la persona a actualizar
- La nueva edad
Tu funciín te debe retornar el diccionario con el cambio hecho
Si el nombre no existe debe mostrar un mensaje indicando que no se encontró
"""

def actualizar_edades(personas, nombre, nueva_edad):
    if nombre in personas:
        personas[nombre] = nueva_edad
    else:
        print("El nombre {} no existe".format(nombre))
    return personas

personas = {"Ana": 26, "Luis": 25, "Carla": 32}
print(actualizar_edades(personas, "Luis", 31))
print(actualizar_edades(personas, "Fiorella", 24))
