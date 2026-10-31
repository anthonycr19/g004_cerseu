"""Diccionarios en Python"""

"""
del: elimina un key y su valor del diccionario
"""

estudiante = {'nombre': "Gustavo", 'edad': 27, 'promedio': 18}

estudiante["distrito"] = "Miraflores"

del estudiante["edad"]
del estudiante["promedio"]
# Si no existe el key el programa se cae o crashea
#del estudiante["hobbie"]
print("Diccionario actualizado: {}".format(estudiante))
