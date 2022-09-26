#Escenario
#   Observa el código en el editor: lee un valor flotante, lo coloca en una variable llamada x,
#   e imprime el valor de la variable llamada y. Tu tarea es completar el código para evaluar la siguiente
#   expresión: 3x³ - 2x² + 3x - 1

# El resultado debe ser asignado a y.

#Prueba de Datos

#Datos de Muestra
#Se asigna los siguientes valores a x (Sustitución)

#x = 0
#x = 1
#x = -1

#Como resultado de la evaluacion debemos obtener lo siguiente
#Salida Esperada

#y = -1.0
#y = 3.0
#y = -9.0

#Solucion...............................

# codifica aquí tus datos de prueba.
print("Ingresa el valor de X: ")
x = float(input())
# escribe tu código aquí.
#3x³ - 2x² + 3x - 1
y = (3 * x ** 3) - (2 * x ** 2) + (3 * x) - 1
print("y =", y)

