#Brian Ulises Orihuela Perez --> 31/07/2022

#----------------------------------Comentarios, Input, concatenacion, replicación-------------------------------------------

#Los comentarios son muy importantes. No solo hacen que el programa sea más fácil de entender, pero también sirven para 
# deshabilitar aquellas partes de código que no son necesarias (por ejemplo, cuando se necesita probar cierta parte del 
# código, e ignorar el resto). Los buenos programadores describen cada parte importante del código, y dan nombres significativos 
# a variables, debido a que en ocasiones es mucho más sencillo dejar el comentario dentro del código mismo.
#---------------------------------------------------------------------------------------------------------------

#este programa calcula los segundos en cierto número de horas determinadas 
# este programa fue escrito hace dos días

a = 2 # numero de horas
segundos = 3600 # número de segundos en una hora

print("Horas: ", a) #imprime el numero de horas
print("Segundos en horas: ", a * segundos) # se imprime el numero de segundos en determinado numero de horas

#aquí también se debe de imprimir un "Adiós", pero el programador no tuvo tiempo de escribirlo
print("Adios amigo")
#este el es fin del programa que calcula el numero de segundos en 2 horas

#input()-------------------------------------------------------------------------------------------

#La función input() es capaz de leer datos que fueron introducidos por el usuario y pasar esos datos al 
# programa en ejecución.
#El programa entonces puede manipular los datos, haciendo que el código sea verdaderamente interactivo.

# print("Dime algo...")
# algo = input()
# print("Mmm...", algo, "...¿en serio?")

#La función input() puede hacer algo más: puede mostrar un mensaje al usuario sin la ayuda de la 
# función print().

algo = input("Dime algo...")
print("Mmm...", algo, "...¿En serio?")

#Se ha dicho antes, pero hay que decirlo sin ambigüedades una vez más: el resultado de la función 
# input() es una cadena.

#Conversión de datos o casting
#int(input()) ó float(input())

algo = float(input("Inserta un número: "))
resultado = algo ** 2.0
print(algo, "al cuadrado es", resultado)

cateto_a = float(input("Inserta la longitud del primer cateto: "))
cateto_b = float(input("Inserta la longitud del segundo cateto "))
hipo = (cateto_a**2 + cateto_b**2) ** .5
print("La longitud de la hipotenusa es: ", hipo)

#concatenando:
nom = input("¿Me puedes dar tu nombre por favor? ")
ape = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias.")
print("\nTu nombre es " + nom + " " + ape + ".")


#Replicación de cadenas 
#El signo de * (asterisco), cuando es aplicado a una cadena y a un número (o a un número y cadena) 
# se convierte en un operador de replicación.

#Imprimiendo un rectangulo
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

#imprimiendo un cuadrado
print("+" + 3 * "-" + "+")
print(("|" + " " * 3 + "|\n"), end="")
#Aqui se pone end dado que en se quiere despreciar el ultimo \n
print("+" + 3 * "-" + "+")

# Función str()

#A estas alturas ya sabes como emplear las funciones int() y float() para convertir una cadena a un número.
#Este tipo de conversión no es en un solo sentido. También se puede convertir un numero a una cadena, 
# lo cual es más fácil y rápido, esta operación es posible hacerla siempre.
#Una función capaz de hacer esto se llama str()

cateto_a = float(input("Ingresa la longitud del primer cateto: "))
cateto_b = float(input("Ingresa la longitud del segundo cateto: "))
print("La longitud de la hipotenusa es: " + str((cateto_a**2 + cateto_b**2) ** .5))

#De esta maner nos ahorramos una linea de codigo en la operación

