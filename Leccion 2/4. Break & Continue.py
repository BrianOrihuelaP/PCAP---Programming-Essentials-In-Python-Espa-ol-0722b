# INSTRUCCIONES BREAK & CONTINUE

# Break: Sale del ciclo inmediatamente, e incondicionalmente termina la operación del ciclo; el programa comienza a 
# ejecutar la instrucción más cercana después del cuerpo del ciclo.
# Continue: Se comporta como si el programa hubiera llegado repentinamente al final del cuerpo; el siguiente turno se inicia y la expresión 
# de condición se prueba de inmediato.

# break - ejemplo

print("La instrucción de ruptura:")
for i in range(1,6):
    if i == 3:
        break
    # Cuando i tenga el valor de 3 entonces se sale del ciclo
    print("Dentro del ciclo.", i)
print("Fuera del ciclo.")

# continua - ejemplo

print("\nLa instrucción continue:")
for i in range(1,6):
    if i == 3:
        continue
    # Cuando i sea igual a 3 entonces  se salta la instruccion y continua el recorrido
    print("Dentro del ciclo.", i)
print("Fuera del ciclo.")

# OTRO EJEMPLO CON BREAK:

numeroMayor = -99999999
contador = 0

while True:
    numero = int (input ("Ingresa un número o escribe -1 para finalizar el programa:"))
    if numero == -1:
        break
    #brake nos arroja un estado false el cual hace que se salga de todo el while
    contador += 1
    if numero > numeroMayor:
        numeroMayor = numero

if contador != 0:
    print("Se han ingresado : ", contador,"números...")
    print("El número más grande es", numeroMayor)
else:
    print("No ha ingresado ningún número") 

# OTRO EJEMPLO CON CONTINUE

# numeroMayor = -99999999
# contador = 0

# numero = int (input("Ingresa un número o escribe -1 para finalizar el programa:"))

# while numero != -1:
#     #Si ingresamos un numero, el while se ejecuta normalmente numero == 5
#     if numero == -1:
#         # numero = 5 no entra al if
#         continue
#     contador += 1
#     #se suma a 1 el contador
#     if numero > numeroMayor:
#         #entra al if y guarda el numero 
#         numeroMayor = numero
#     numero = int (input ("Ingresa un número o escribe -1 para finalizar el programa:"))

# if contador:
#     print("Se ha ingresado ",contador,"numeros...")
#     print("El número más grande es", numeroMayor) 
# else: #si la primera ejecucion es -1 entonces contador es 0 y es igual a false
#     print("No ha ingresado ningún número") 