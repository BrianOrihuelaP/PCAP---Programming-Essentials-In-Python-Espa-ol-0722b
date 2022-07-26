# Escenario
# La sentencia continue se usa para omitir el bloque actual y avanzar a la siguiente iteración, sin ejecutar las declaraciones 
# dentro del ciclo.

# Se puede usar tanto con while y ciclos for.

# Tu tarea aquí es muy especial: ¡Debes diseñar un devorador de vocales! Escribe un programa que use:

# Un ciclo for.
# El concepto de ejecución condicional (if-elif-else).
# La declaración continue.
# Tu programa debe:

# Pedir al usuario que ingrese una palabra.
# Utiliza userWord = userWord.upper() para convertir la palabra ingresada por el usuario a mayúsculas; hablaremos 
# sobre los llamados métodos de cadena y el upper() muy pronto, no te preocupes.
# Utiliza la ejecución condicional y la instrucción continue para "comer" las siguientes vocales A , E , I , O , U 
# de la palabra ingresada.
# Imprime las letras no consumidas en la pantalla, cada una de ellas en una línea separada.

# Prueba tu programa con los datos que le proporcionamos.

# Datos de prueba
# Entrada de muestra: Gregory

# Salida esperada:

# G
# R
# G
# R
# Y
# Entrada de muestra: abstemious

# Salida esperada:

# B
# S
# T
# M
# S

# Entrada de muestra: IOUEA

# Salida esperada: empty

 #CODE ----------------------------------------------------------

 # Indicar al usuario que ingrese una palabra
# y asignarlo a la variable userWord.
import pyfiglet
ASCII_art_0 = pyfiglet.figlet_format("ORI - DEVORA VOCALES :v")

print(ASCII_art_0)

comando = 0
userWord = input("Porfavor ingresa una palabra: ").upper()

while True:
    for letra in userWord:
        # Completa el cuerpo del ciclo for.
        if letra == "A":
            continue
        elif letra == "E":
            continue
        elif letra == "I":
            continue
        elif letra == "O":
            continue
        elif letra == "U":
            continue
        print(letra  + "\n")
    comando = input("Desea continuar??? \n 1. Continuar    2. Salir del pograma: ")
    if comando != "2":
        userWord = input("Porfavor ingresa una palabra: ").upper()
    else:
        break

 