"""Diccionarios en Python"""

"""
values: obtener los valores de los keys de un diccionario
"""

base_datos = {"nombre": "Mysql", "tipo": "BD relacional", "gestor_bd": "workbench"}

"""conversión de diccionarios a listas"""

base_datos_list = list(base_datos)
print("Diccionario convertido en lista: {}".format(base_datos_list))

base_datos_values = list(base_datos.values())
print("Values: {}".format(base_datos_values))

base_datos_keys = list(base_datos.keys())
print("Key: {}".format(base_datos_keys))

base_datos_items = list(base_datos.items())
print("Items: {}".format(base_datos_items))