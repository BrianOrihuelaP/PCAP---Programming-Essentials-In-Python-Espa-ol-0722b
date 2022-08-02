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