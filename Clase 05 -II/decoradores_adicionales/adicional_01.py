""""
Requisitos:
* Se creará una función decoradora llamada analizar_texto
* Crear una función que recibirá un string como argumento de la función decorada
* Tu función decoradora contará la cantidad total de caracteres (sin espacio)
* Tu función decoradora contará el número total de caracteres
* La función a decorar se llamará mostrar_texto(texto) e imprimirá el texto pasado por argumento
"""


def analizar_texto(func):
    def funcionIntermedia(texto):
        caracteres = len(texto.replace(" ", ""))  # Contar caracteres sin espacios
        palabras = len(texto.split()) # Contar palabras

        print("* Palabras: {}".format(palabras))
        print("* Caracteres (sin contar espacios): {}".format(caracteres))

        # Ejecutar la función original
        return func(texto)
    return funcionIntermedia


@analizar_texto
def mostrar_texto(texto):
    print("Texto: {}".format(texto))


# Pruebas
mostrar_texto("Aprender Machine Learning con Python")
mostrar_texto("Los decoradores permiten escribir código muy elegante")