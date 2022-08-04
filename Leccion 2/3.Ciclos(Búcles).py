# Bucles

# La ejecución de una determinada parte del código más de una vez se denomina bucle.

# lee tres números
numero1 = int(input("Ingresa el primer número:"))
numero2 = int(input("Ingresa el segundo número:"))
numero3 = int(input("Ingresa el tercer número:"))

# verifica cuál de los números es el mayor
# y pásalo a la variable de mayor número

numeroMayor = max(numero1,numero2,numero3)
# La función max retorna el mayor de tres números

# imprimir el resultado
print("El número más grande es:", numeroMayor) 

# De la misma manera, puedes usar la función min() para devolver el número más bajo.

# WHILE *******************************************************************
# "mientras haya algo que hacer hazlo"

# while expresión_condicional:
# instrucción

# Un ciclo infinito, también denominado ciclo sin fin, es una secuencia de instrucciones en un programa que se repite indefinidamente (ciclo sin fin).

# Este es un ejemplo de un ciclo que no puede finalizar su ejecución:

# while True:
#     print("Estoy atrapado dentro de un ciclo")

# Ejemplo: 
# Almacenaremos el número más grande actual aquí
print("*WHILE*")
numeroMayor = -999999999

# Ingresa el primer valor
numero = int(input ("Introduzca un número o escriba -1 para detener:"))

# Si el número no es igual a -1, continuaremos
while numero != -1:
    # ¿Es el número más grande que el número más grande?
    if numero > numeroMayor:
        # Sí si, actualiza el mayor númeroNúmero
        numeroMayor = numero
    # Ingresa el siguiente número
    numero = int (input("Introduce un número o escribe -1 para detener:"))
    # Aquí ingresamos otro numero ya sea 2,4,56 y este se volvera a guardar en numero
    # Se regresa a la condicion while y si cumple vuelve a hacer lo mismo y asi hasta que numero sea -1
# Imprimir el número más grande
print("El número más grande es:", numeroMayor)

# EJERCICIO 3.1.2.2

# programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares
# programa termina cuando se ingresa cero

numerosImpares = 0
numerosPares = 0

# lee el primer número
numero = int (input ("Introduce un número o escriba 0 para detener:"))

# 0 termina la ejecución
while numero != 0:
    # verificar si el número es impar
    if numero % 2 == 1:
        # aumentar el contador de números impares
        numerosImpares += 1
    else:
        # aumentar el contador de números pares
        numerosPares += 1
    # lee el siguiente número
    numero = int (input ("Introduce un número o escriba 0 para detener:"))

# imprimir resultados
print("Números impares: ", numerosImpares)
print("Números pares: ", numerosPares)

# FOR *******************************************************************

# Otro tipo de ciclo disponible en Python proviene de la observación de que a veces es más importante contar los "giros o vueltas" 
# del ciclo que verificar las condiciones.

# Imagina que el cuerpo de un ciclo debe ejecutarse exactamente cien veces. Si deseas utilizar el ciclo while para hacerlo, 
# puede tener este aspecto:

# i = 0
# while i < 100:
#     # hacer_algo()
#     i += 1 

# for está diseñado para realizar tareas más complicadas, puede "explorar" grandes colecciones de datos elemento por elemento. Te mostraremos como hacerlo pronto, pero ahora presentaremos una variante más sencilla de su aplicación.

# Echa un vistazo al fragmento:

#  for i in range (100):
#     #hacer algo()
#     pass

print("FOR.......................")
# Ejemplo:

for i in range(10):
    print("El valor de i es actualmente", i)
# Esto imprime 10 veces el valor de i de uno en uno del 0 al 9
print()
for i in range (2, 8):
    print("El valor de i es actualmente", i)
# Esto imprime 6 veces el valor de i de uno en uno del 2 al 7

# Nota: la función range() solo acepta enteros como argumentos y genera secuencias de enteros.

for i in range(2, 8, 3):
    print("El valor de i es actualmente", i)

# El tercer argumento es un incremento: es un valor agregado para controlar la variable en cada giro del ciclo 
# (como puedes sospechar, el valor predeterminado del incremento es 1 ).

# El primer argumento pasado a la función range() nos dice cual es el número de inicio de la secuencia (por lo tanto, 
# 2 en la salida). El segundo argumento le dice a la función dónde detener la secuencia (la función genera números hasta el 
# número indicado por el segundo argumento, pero no lo incluye). Finalmente, el tercer argumento indica el paso, 
# que en realidad significa la diferencia entre cada número en la secuencia de números generados por la función.

# for i in range(2, 1):
    # print ("El valor de i es actualmente", i) 
# Lo anterior es invalido, dado que range debe de tener un orden ascendente no descendente 

#Echemos un vistazo a un programa corto cuya tarea es escribir algunas de las primeras potencias de dos:

pow = 1
for exp in range(16):
    print ("2 a la potencia de", exp, "es", pow)
    pow *= 2 

# Salida exp = 1 : 1, exp = 2 : 2; exp = 3 : 4, ...

# La variable exp se utiliza como una variable de control para el ciclo e indica el valor actual del exponente. 
# La propia exponenciación se sustituye multiplicando por dos. Dado que 2 0 es igual a 1, después 2 × 1 es igual a 21, 2 × 21 
# es igual a 22, y así sucesivamente.

