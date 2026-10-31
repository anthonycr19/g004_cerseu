"""


"""


import math

def validar_numero(func):
    def funcionIntermedia(num):
        if num < 0:
            print("Error: el número {} es negativo. No se puede calcular la raíz cuadrada.".format(num))
            return None
        else:
            print("Número válido: {}".format(num))
            return func(num)
    return funcionIntermedia


@validar_numero
def raiz_cuadrada(num):
    resultado = math.sqrt(num)
    print("La raíz cuadrada de {} es {}".format(num, resultado))


# Realizando pruebas
raiz_cuadrada(10)
raiz_cuadrada(0)
raiz_cuadrada(-7)
raiz_cuadrada(25)