"""Listas en python"""
"""
Listas,
copy(): Copia todos los elementos de una lista a otra nueva lista
"""

var_1 = ["SQLServer", "Sas", "RDS", "Mysql", "PostgreSQL", "MariaDB"]

var_2 = var_1.copy()

print("Elementos de mi nueva lista: {}".format(var_2))

var_2.append("SQLite3")
var_2.append("33")
var_2.pop(1)
print("Mi lista clon actualizada: {}".format(var_2))

print("Lista original: {}".format(var_1))