#  Hay dos tipos de ciclos en Python: while y for:

# El ciclo while ejecuta una sentencia o un conjunto de declaraciones siempre que una condición booleana especificada sea verdadera, 
# por ejemplo:

# Ejemplo 1
# while True:
#     print("Atascado en un ciclo infinito")

# Ejemplo 2
contador = 5
while contador > 2:
    print(contador)
    contador -= 1

# El ciclo for ejecuta un conjunto de sentencias muchas veces; se usa para iterar sobre una secuencia (por ejemplo, una lista, 
# un diccionario, una tupla o un conjunto; pronto aprenderás sobre ellos) u otros objetos que son iterables (por ejemplo, cadenas). 
# Puedes usar el ciclo for para iterar sobre una secuencia de números usando la función incorporada range. Mira los ejemplos a
#  continuación:
print("\n")
# Ejemplo 1
palabra = "Python"
for letter in palabra:
    print(letter, end="*")


print("\n")
# Ejemplo 2
for i in range(1, 10):
    # Recorre empezando en el 1 y parando en el 10
    if i % 2 == 0:
        #Imprime solo los pares 
        print(i)

# 2. Puedes usar las sentencias break y continue para cambiar el flujo de un ciclo:
# Utiliza break para salir de un ciclo, por ejemplo:
print(" \n Part 2 *************")
texto = "OpenEDG Python Institute"
# ciclo que recorrera  con la ayuda de la variable letter 
for letter in texto:
    if letter == "P":
        # en el momento que se encuentre una p mayuscula se rompe el ciclo
        break
    print(letter, end= "")
    # para una impresion continua sin salto se usa end = ""

# Utiliza continue para omitir la iteración actual, y continuar con la siguiente iteración, por ejemplo:
print("\n")
text = "pyxpyxpyx"
# ciclo que recorrera  con la ayuda de la variable letter 
for letter in text:
    # si se encuentra una x esta se la salta y continua el recorrido
    if letter == "x":
        continue
    print(letter, end= "")

# 3. Los ciclos while y for también pueden tener una cláusula else en Python. La cláusula else se ejecuta después de que el ciclo
#  finalice su ejecución siempre y cuando no haya terminado con break, por ejemplo:
print("\n")
n = 0
while n != 3:
    print(n)
    n += 1
else:
    print(n, "else")
    #aqui vale tres por que en la ultima iteracion primero incrementa a 3 para cerrar el ciclo
print()

for i in range(0, 3):
    print(i)
    #Aqui vale 2 por que el ciclo para en 2 (0,1,2)
else:
    print(i, "else")

# 4. La función range() genera una secuencia de números. Acepta enteros y devuelve objetos de rango. La sintaxis de range() 
# tiene el siguiente aspecto: range(start, stop, step), donde:

# start es un parámetro opcional que especifica el número de inicio de la secuencia (0 por defecto).
# stop es un parámetro opcional que especifica el final de la secuencia generada (no está incluido).
# y step es un parámetro opcional que especifica la diferencia entre los números en la secuencia es (1 por defecto).
# Código de ejemplo:
print("----------------")
for i in range(3):
    print(i, end=" ") # salidas: 0 1 2
print()
for i in range(6, 1, -2):
    # el ciclo es de decremento empieza en el 6 y termina en 2
    # Los ciclos de decremento siempre necesitan el step para iterar
    print(i, end=" ") # salidas: 6, 4, 2

# continuar en 3.1.2.17
