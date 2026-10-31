"""Listas en python"""

"""
Lista: Recorrido de las listas en un búcle for
"""

notas = [12, 18, 16, 20, 11, 14, 13]

i = 0
for nota in notas:
    #print(nota)
    #print("Nota: {}".format(nota))
    print(notas[i])
    notas[i] = nota - 2
    print("Nota actualizada: {}".format(notas[i]))
    i = i + 1 # aumenta en 1 el valor de i

print(notas)

# La nueva lista actualizada tendrá la mitad del valor de cada nota
# agregar dos notas en la lista que sean mayores a las notas de la lista actualizada
