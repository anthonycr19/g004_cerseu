"""Diccionarios en Python"""

"""
sorted: obtener los nombres de los keys de un diccionario
"""

base_datos = {"nombre": "Mysql", "tipo": "BD relacional", "gestor_bd": "workbench"}

keys = sorted(base_datos)
print(base_datos)
print(keys)

base_datos_keys_set = base_datos.keys()
print("conjuntos keys: {}".format(base_datos_keys_set))
base_datos_keys = list(base_datos.keys())
print("keys: {}".format(base_datos_keys))
