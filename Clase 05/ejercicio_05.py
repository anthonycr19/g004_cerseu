"""
    POO
    Encapsulamiento
"""

class A:
    def __init__(self):
        self.inicial = 5
        self._contador = 0

    def incremeta(self):
        self._contador = self._contador + 1

    def cuenta(self):
        return self._contador

class B:
    def __init__(self):
        self.inicial = True
        self.__contador = 0  #Atributo privado

    def incrementa(self):
        self.__contador = self.__contador + 1

    def cuenta(self):
        return self.__contador

var_1 = A()
var_1._contador
var_1.inicial = 20

var_1.incremeta()
var_1.incremeta()
var_1.incremeta()

print(var_1.cuenta())
print("Valor inicial de A: {}".format(var_1.inicial))

var_2 = B()
var_2.inicial  =False

var_2.incrementa()
var_2.incrementa()
var_2.incrementa()
var_2.incrementa()

print("Valor de contador B es: {}".format(var_2.cuenta()))
print("Valor inicial de B es: {}".format(var_2.inicial))


print(var_2.__contador)


