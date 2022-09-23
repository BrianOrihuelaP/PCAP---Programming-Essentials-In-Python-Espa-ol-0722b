# ESCENARIO 2

# La tarea es completar el código para poder evaluar la siguiente expresión:
# Vease la imagen 2.1.6.10 disponible en la carpeta img del repositorio...

#Entrada de muestra: 1
# Salida esperada:
# y = 0.6000000000000001

# Entrada de muestra: 10
# Salida esperada:
# y = 0.09901951266867294

# Entrada de muestra: 100
# Salida esperada:
# y = 0.009999000199950014

# Entrada de muestra: -5
# Salida esperada:
# y = -0.19258202567760344

#SOLUCION: 

x = float(input("Ingresa el valor para x: "))

# coloca tu código aquí
y = 1 / (x + 1 / (x + 1 / (x + 1 / x)))

print("y =", y)