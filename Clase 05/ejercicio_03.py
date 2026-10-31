"""
Programación orientada a objetos
"""

class Carro:
    """atributos"""
    ruedas = 4
    """Constructor: Valores que van a tener por defecto mi clase que se isntanacia en una variable"""
    def __init__(self, color, aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0

    """Métodos: Son las funciones de las clases"""
    def acelerar(self):
        self.velocidad = self.velocidad + self.aceleracion

    def frenar(self):
        velocidad = self.velocidad - self.aceleracion
        if velocidad < 0:
            velocidad = 0
        self.velocidad = velocidad


class CarroVolador(Carro):
    ruedas = 6

    def __init__(self, color, aceleracion, estado_volando=False):
        super().__init__(color, aceleracion)
        self.color = color
        self.aceleracion = aceleracion
        self.estado_volando = estado_volando

    def vuela(self):
        self.estado_volando = True

    def aterriza(self):
        self.estado_volando = False

carro_1 = Carro("negro", 69)
carro_volador = CarroVolador("Blanco", 35)

print("Color del carro volador: {}".format(carro_volador.color))
print("El estado actual del carro volador está en: {}".format(carro_volador.estado_volando))

carro_volador.vuela()
carro_volador.acelerar()
carro_volador.acelerar()
carro_volador.acelerar()

carro_volador.frenar()
carro_volador.frenar()

print("La velocidad actual del carro volador: {}".format(carro_volador.velocidad))

"""Esto no será posible, porque la herencia es solo de la clase HIJA, y no de la clase PADRE"""
#carro_1.vuela()