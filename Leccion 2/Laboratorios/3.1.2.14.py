# LAB 3.1.2.14

# Objetivos
# Familiarizar al estudiante con:

# Utilizar el ciclo while.
# Encontrar la implementación adecuada de reglas definidas verbalmente.
# Reflejar situaciones de la vida real en código de computadora.

# Escenario -------------------------

# Escucha esta historia:
# Un niño y su padre, un programador de computadoras, juegan con bloques de madera. Están construyendo una pirámide.
# Su pirámide es un poco rara, ya que en realidad es una pared en forma de pirámide, es plana. La pirámide se apila 
# de acuerdo con un principio simple: cada capa inferior contiene un bloque más que la capa superior.
# La figura ilustra la regla utilizada por los constructores: ver img 3.1.2.14

# Tu tarea es escribir un programa que lea la cantidad de bloques que tienen los constructores, y generar la altura de la 
# pirámide que se puede construir utilizando estos bloques.

# Nota: La altura se mide por el número de capas completas: si los constructores no tienen la cantidad suficiente de bloques
# y no pueden completar la siguiente capa, terminan su trabajo inmediatamente.

# Prueba tu código con los datos que hemos proporcionado.

# Datos de prueba -----------------------------

# Entrada de muestra: 6
# Producto esperado: La altura de la pirámide es: 3

# Entrada de muestra: 20
# Salida esperada: La altura de la pirámide es: 5

# Entrada de muestra: 1000
# Resultado esperado: La altura de la pirámide es: 44

# Entrada de muestra: 2
# Salida esperada: La altura de la pirámide es: 1
import pyfiglet
ASCII_art_0 = pyfiglet.figlet_format("ORI - MY PIRAMID")

print(ASCII_art_0)
bloques = int(input("Ingrese el número de bloques:"))

capa = 1 #variable la cual tomara n bloques para cada capa 
#(capa 1 = 1 bloque, capa 2 = 2 bloques, capa 3 = 3 bloques, capa 4 = 4 bloques)
altura = 0
# variable la cual aumentaremos por cada capa
# Escribe tu código aquí.
while True: # Ejecutame x hasta que exista un break
   if bloques <= 0: # verifico si todavia tengo bloques para crear mas capas
       break #  si no me quedan bloques entonces rompo el ciclo
   else:
        bloques = bloques - capa 
        # A mi numero total de bloques quitame los que se nesecitan en la capa y ese se resultado se guarda en mis bloques totales
        print( "x" * capa)
        capa += 1 # Aumentamos en una unidad las capas
        altura += 1 #priero validamos que tengamos bloques y agregamos la altura o nivel de la piramide 
        
print("La altura de la pirámide:", altura)
