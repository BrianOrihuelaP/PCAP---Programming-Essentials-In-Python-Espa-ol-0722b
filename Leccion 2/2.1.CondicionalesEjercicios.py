# Analizando ejemplos de código -> 3.1.1.9 PCAP

# Ahora te mostraremos algunos programas simples pero completos. No los explicaremos en detalle, 
# porque consideramos que los comentarios (y los nombres de las variables) dentro del código son guías 
# suficientes.

# Todos los programas resuelven el mismo problema: encuentran el número mayor y lo imprimen.

# Ejemplo 1:

# Comenzaremos con el caso más simple: ¿Cómo identificar el mayor de los dos números? :

# lee dos números
numero1 = int (input("Ingresa el primer número: "))
numero2 = int (input("Ingresa el segundo número: "))

#elegir el número más grande
if numero1 > numero2:
    nmasGrande = numero1
else:
    nmasGrande = numero2

#imprimir el resultado
print("El número más grande es:", nmasGrande)

# El fragmento de código anterior debe estar claro: lee dos valores enteros, los compara y 
# encuentra cuál es el más grande.

# Ejemplo 2:

# Ahora vamos a mostrarte un hecho intrigante. Python tiene una característica interesante, 
# mira el código a continuación:

#lee dos números
numero1 = int (input("Ingresa el primer número:"))
numero2 = int (input("Ingresa el segundo número:"))

# elegir el número más grande
if numero1 > numero2: nmasGrande = numero1
else: nmasGrande = numero2

#imprimir el resultado
print("El número más grande es: ", nmasGrande)

# Nota: si alguna de las ramas de if-elif-else contiene una sola instrucción, puedes codificarla de forma más 
# completa (no es necesario que aparezca una línea con sangría después de la palabra clave), pero solo continúa 
# la línea después de los dos puntos).
# Sin embargo, este estilo puede ser engañoso, y no lo vamos a usar en nuestros programas futuros, 
# pero definitivamente vale la pena saber si quieres leer y entender los programas de otra persona.

# Ejemplo 3:

# Es hora de complicar el código: encontremos el mayor de los tres números. ¿Se ampliará el código? Un poco.
# Suponemos que el primer valor es el más grande. Luego verificamos esta hipótesis con los dos valores restantes.
# Observa el siguiente código:

#lee tres números
numero1 = int (input("Ingresa el primer número:"))
numero2 = int (input("Ingresa el segundo número:"))
numero3 = int (input("Ingresa el tercer número:"))

#asumimos temporalmente que el primer número
#es el más grande
#lo verificaremos pronto
nmasGrande = numero1

#comprobamos si el segundo número es más grande que el mayor número actual
#y actualiza el número más grande si es necesario
if numero2 > nmasGrande:
    nmasGrande = numero2

#comprobamos si el tercer número es más grande que el mayor número actual
#y actualiza el número más grande si es necesario
if numero3 > nmasGrande:
    nmasGrande = numero3

#imprimir el resultado
print("El número más grande es:", nmasGrande)