# OPERADORES-------------------------------------------------------------------------
# Un operador es un símbolo del lenguaje de programación, el cual es capaz de realizar operaciones con los valores.

# Por ejemplo, como en la aritmética, el signo de + (mas) es un operador el cual es capaz de sumar dos numeros, dando el resultado de la suma.
# Sin embargo, no todos los operadores de Python son tan simples como el signo de mas, veamos algunos de los operadores disponibles en Python,
# las reglas que se deben seguir para emplearlos, y como interpretar las reglas que realizan.

# Se comenzará con los operadores que están asociados con las operaciones aritméticas más conocidas:
# +, -, *, /, //, %, **

print("Suma: ", 2+2)
print("Resta: ", 10-6)
print("Multiplicación: ", 3*4)
print("Divición: ", 23/10)
print("División entera: ", 100//20)

# Exponenciación....................
print("Exponencial: ", 2 ** 4)
print(2 ** 3)  # entero
print(2 ** 3.)  # decimal
print(2. ** 3)  # decimal
print(2. ** 3.)  # decimal

# Modulo.......................
print("Modúlo 10 * 3: ", 10 % 3)
print("Modulo de 14 % 4 : ", (14 % 4))
print("Modulo de 12 % 4.5 : ", (15 % 4.5))

# El operador de resta, operadores unarios y binarios
print(-4 - 4)
print(4. - 8)
print(-1.1)

# Operadores y sus enlaces
# El enlace de un operador determina el orden en que se computan las operaciones de los operadores con la misma prioridad,
# los cuales se encuentran dentro de una misma expresión.
# La mayoría de los operadores de Python tienen un enlazado hacia la izquierda, lo que significa que el calculo de la
# expresión es realizado de izquierda a derecha.

print("Jerarquia:")
print(5*3*2)

# El resultado debe ser 1. El operador tiene un enlazado hacia la izquierda. Pero hay una excepción interesante.
print('Enlazado de: "9 % 6 % 2 :"')
res = 9 % 6
print("primero: 9 % 6 ->", res)
print('despues: ', res, " % 2: ", res % 2)
print('Resultado esperado: ', 9 % 6 % 2)

# Exponenciación y sus enlaces :
print(2 ** 2 ** 3)
# Se resuelve tal y como en matematicas por ley de los exponentes:
# se tiene la base 2 la cual esta elevada : 2³
# se resuelve primero la exponencial y luego se aplica a la base

print('Enlazado de: "2 * 3 % 5 :"')
res = 2 * 3
print("primero: 2 * 6 ->", res)
print('despues: ', res, " % 5: ", res % 5)
print('Resultado esperado:',2 * 3 % 5)
# La presente operacion contiene operadores con la misma prioridad, es aqui donde se aplica el emlazado de Izq a der.

print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
# de igual manera se aplica jerarquia

# Un operador unario es un operador con solo un operando, por ejemplo, -1, o +3.
# Un operador binario es un operador con dos operados, por ejemplo, 4+5, o 12%5.
