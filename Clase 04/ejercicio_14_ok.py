"""Uso de cond. if"""

var_1, var_2, var_3 = 80, 150.9, "Python"

if var_1 == 50 and var_2 > 40 or var_3 == "Python": # T and T or T -> T or T -> T
    print("1. Ingresó a la condicional triple")
else:
    print("2. Ingresó al else")

"""
Nota:
- Los resultados de las condiciones se van a agrupar de izquierda a derecha
"""