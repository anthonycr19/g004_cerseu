"""
    POO
    Polimorfismo
"""

class Perro():
    def sonido(self):
        print("Guauuuu")


class Gato():
    def sonido(self):
        print("Miauuu")


class Vaca():
    def sonido(self):
        print("Muuuu")


gato = Gato()
perro = Perro()
vaca = Vaca()

lista_animals = [gato, perro, vaca]

def canto(animales):
    for animal in animales:
        animal.sonido()

canto(lista_animals)
