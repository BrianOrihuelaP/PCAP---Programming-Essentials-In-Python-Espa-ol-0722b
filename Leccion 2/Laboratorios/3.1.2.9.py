# Escenario:

# La instrucción break se usa para salir/terminar un ciclo.

# Diseña un programa que use un ciclo while y le pida continuamente al usuario que ingrese una palabra a menos
#  que ingrese "chupacabra" como la palabra de salida secreta, en cuyo caso el mensaje 
# "¡Has dejado el ciclo con éxito". Debe imprimirse en la pantalla y el ciclo debe terminar.
# No imprimas ninguna de las palabras ingresadas por el usuario. Utiliza el concepto de ejecución condicional 
# y la declaración break.
import pyfiglet

ASCII_art_0 = pyfiglet.figlet_format("ORI - Halloween Eve")
ASCII_art_1 = pyfiglet.figlet_format("Has dejado el ciclo con exito!")
print(ASCII_art_0)

while True:
    palabra = input("Ingresa mounstros famosos de Halloween: ")
    if palabra == "chupacabras":
        print(ASCII_art_1)
        break




