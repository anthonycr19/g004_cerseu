"""Listas en python"""
"""
Listas,
del: Eliminar un valor indicando un índice de la lista
"""

paises = []
paises.append("Perú")
paises.append("Brasil")

#2da forma para agregar valores a una lista (más reducido)
paises.extend(["Colombia", "Mexico", "Canadá", "Alemania", "Francia"])

print("Mi lista tiene los valores: {}".format(paises))

del paises[2]
print("Mi lista actualizada: {}".format(paises))

del paises[4]
print("Mi lista actualizada: {}".format(paises))
