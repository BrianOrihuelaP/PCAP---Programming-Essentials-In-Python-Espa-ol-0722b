# Escenario

# Espatifilo, más comúnmente conocida como la planta de Cuna de Moisés o flor de la paz, es una de las plantas 
# para interiores más populares que filtra las toxinas dañinas del aire. Algunas de las toxinas que neutraliza 
# incluyen benceno, formaldehído y amoníaco.

# Imagina que tu programa de computadora ama estas plantas. Cada vez que recibe una entrada en forma de la 
# palabra Espatifilo, grita involuntariamente a la consola la siguiente cadena:  "¡Espatifilo es la mejor 
# planta de todas!" 

# Escribe un programa que utilice el concepto de ejecución condicional, tome una cadena como entrada y que:

# Escribe un programa que utilice el concepto de ejecución condicional, tome una cadena como entrada y que:

# Imprima el enunciado "Si, ¡El Espatifilo es la mejor planta de todos los tiempos!" en la 
# pantalla si la cadena ingresada es "Espatifilo".
# Imprima "No, ¡quiero un gran Espatifilo!" si la cadena ingresada es "espatifilo".
# Imprima  "¡Espatifilo! ¡No [entrada]!"  de lo contrario. Nota: [entrada] es la cadena que se toma como entrada.

#DATOS DE PRUEBA: 
# Entrada de muestra: espatifilo
# Resultado esperado: No, ¡quiero un gran Espatifilo!

# Entrada de ejemplo: pelargonio
# Resultado esperado: !Espatifilo! ¡No pelargonio!

# Entrada de muestra: Espatifilo
# Resultado esperado: Si, ¡El Espatifilo es la mejor planta de todos los tiempos!

# SOLUCION: 

inPlanta = input("Ingresa el nombre de la planta que quieres: ")

if inPlanta == "Espatifilo":
    print("Si, ¡El Espatifilo es la mejor planta de todas!")
elif inPlanta == "espatifilo":
    print("No, ¡quiero un gran Espatifilo!")
else:
    print("¡Espatifilo!" + "¡No " + inPlanta + "!")