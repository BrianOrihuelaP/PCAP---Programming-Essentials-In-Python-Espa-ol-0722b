# Escenario
# Un mago junior ha elegido un número secreto. Lo ha escondido en una variable llamada númeroSecreto. Quiere que todos los que
# ejecutan su programa jueguen el juego Adivina el número secreto, y adivina qué número ha elegido para ellos.
# ¡Quienes no adivinen el número quedarán atrapados en un ciclo sin fin para siempre! Desafortunadamente, él no sabe cómo completar el código.

# Tu tarea es ayudar al mago a completar el código en el editor de tal manera que el código:

# Pedirá al usuario que ingrese un número entero.
# Utilizará un ciclo while.
# Comprobará si el número ingresado por el usuario es el mismo que el número escogido por el mago. Si el número elegido por el
# usuario es diferente al número secreto del mago, el usuario debería ver el mensaje "¡Ja, ja! ¡Estás atrapado en mi ciclo!"
# y se le solicitará que ingrese un número nuevamente. Si el número ingresado por el usuario coincide con el número escogido por el mago,
#  el número debe imprimirse en la pantalla, y el mago debe decir las siguientes palabras: "¡Bien hecho, muggle! Eres libre ahora".

# SOLUCION:
import time
import pyfiglet

# Debemos de instalar la dependencia (libreria) pyfiglet para las animaciones de consola con pip install 

numeroSecreto = 777
maldicion = "Avada Kedavra"
secret = "Alohomora"

T = "ORI - GAME"
ASCII_art_0 = pyfiglet.figlet_format(T)
print(ASCII_art_0)

name = input("Hola hechizero, ingresa tu nombre: ")


T = "AVADA KEDAVRA"
ASCII_art_1 = pyfiglet.figlet_format(T,font='isometric1')


print(
    """
+==================================+
| Bienvenido a mi juego, muggle!   |
| Soy Tom Riddle...                |
| Esta es la prueba uno:           |       
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Pista: HP Libros  333            |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

numero = int(input("Muggle, ingresa tu preddición del número: "))

while numero != numeroSecreto:
    print("CRUCIO!!! ; ¡Ja, ja! ¡Estás atrapado en mi ciclo!")
    for i in range(20):
        time.sleep(0.5)
        print("""
        ||||||||||||||||||||||||||||||
        |||||||||||||°|°||||||||||||||
        ||||||||||||°°|°°|||||||||||||
        |||||||||||°°°|°°°||||||||||||
        ||||||||||°°++|++°°|||||||||||
        |||||||||°°+++|+++°°||||||||||
        ||||||||°°°°++|++°°°°|||||||||
        |||||||°°°°°°°|°°°°°°°||||||||
        """)

    numero = int(
        input("Muggle, ingresa nuevamente tu preddición del número: "))


print("¡Bien hecho, muggle! Pasaste la primera prueba....")


print(
    """
+==================================+
| Esta es la segunda prueba:       |       
| Como se llama la maldicion que   |
| yo Tom Riddle le aplique a harry |
| y como resutado tiene una        |
| cicatriz,                        |
| ¿Cuál es esa maldición?          |
+==================================+
""")

respuesta = input("Escribe la maldición que tu piensas es la respuesta: ")

while respuesta != maldicion:
    print("CRUCIO!!! ; ¡Ja, ja! ¡Sigues atrapado en mi ciclo!")
    for i in range(20):
        time.sleep(0.3)
        print("""
        ||||||||||||||||||||||||||||||
        |||||||||||||°|°||||||||||||||
        ||||||||||||°°|°°|||||||||||||
        |||||||||||°°°|°°°||||||||||||
        ||||||||||°°++|++°°|||||||||||
        |||||||||°°+++|+++°°||||||||||
        ||||||||°°°°++|++°°°°|||||||||
        |||||||°°°°°°°|°°°°°°°||||||||
        """)
    print("¡Muggle!, vuelve a intentarlo....")
    respuesta = input("Escribe la maldición que tu piensas es la respuesta: ")

print("¡Bien hecho, muggle! Pasaste la segunda prueba....")


print(
    """
+==================================+
| Esta es la última prueba:        |       
| Si Hermione estuviese atrapada   |
| y no hay manera de como salirse, |
| que aría? jajaja!                |
| Pienza!!!                        |
| Ahora tu estas atrapado          |
| ¡¡¡¡¡¡¡¡¡¡Fermaportus!!!!!       |
+==================================+
""")

respuesta = input("Escribe un hechizo para salirte del bucle: ")
intentos = 0
while respuesta != secret:
    print("CRUCIO!!! ; ¡Ja, ja! ¡Sigues atrapado en mi ciclo!")
    intentos += 1
    for i in range(20):
        time.sleep(0.3)
        print("""
        ||||||||||||||||||||||||||||||
        |||||||||||||°|°||||||||||||||
        ||||||||||||°°|°°|||||||||||||
        |||||||||||°°°|°°°||||||||||||
        ||||||||||°°++|++°°|||||||||||
        |||||||||°°+++|+++°°||||||||||
        ||||||||°°°°++|++°°°°|||||||||
        |||||||°°°°°°°|°°°°°°°||||||||
        """)
    print("¡Muggle!, vuelve a intentarlo....")
    respuesta = input("Escribe un hechizo para salirte del bucle: ")

    if intentos == 2:
        print(ASCII_art_1)
        print("""

        ||||||||||||||||||||||||||||||
        |||||||||||||°|°||||||||||||||
        ||||||||||||°°|°°|||||||||||||
        |||||||||||°°°|°°°||||||||||||
        ||||||||||°°++|++°°|||||||||||
        |||||||||°°+++|+++°°||||||||||
        ||||||||°°°°++|++°°°°|||||||||
        |||||||°°°°°°°|°°°°°°°||||||||
        
        PERDISTE CONTRA VOLDEMORT
        
        """
              )
        break

if intentos == 2:
    print("RIP hecizero: " + name)
else:
    print(ASCII_art_1)
    print("¡NOOOO!....\n Bien hecho derrotaste a voldemort....")
