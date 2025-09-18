"""Listas en python"""

"""
Listas,
remove(): Elimina un elemento de la lista, indicando el valor
"""

var_1 = ["Python", "Javascript", "Java", "PHP", "Typescript"]

print("Los valores de mi lista son: {}".format(var_1))

var_1.remove("Python")
var_1.remove("Java")

print("Mi lisa actualizada: {}".format(var_1))
print(var_1)