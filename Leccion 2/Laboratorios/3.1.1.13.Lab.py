# Escenario

# Como seguramente sabrás, debido a algunas razones astronómicas, el año pueden ser bisiesto o común.
# Los primeros tienen una duración de 366 días, mientras que los últimos tienen una duración de 365 días.
# Desde la introducción del calendario gregoriano (en 1582), se utiliza la siguiente regla para determinar el tipo de año:

# Si el número del año no es divisible entre cuatro, es un año común.
# De lo contrario, si el número del año no es divisible entre 100, es un año bisiesto.
# De lo contrario, si el número del año no es divisible entre 400, es un año común.
# De lo contrario, es un año bisiesto.
# Observa el código en el editor: solo lee un número de año y debe completarse con las instrucciones que implementan la 
# prueba que acabamos de describir.

# El código debe mostrar uno de los dos mensajes posibles, que son Año bisiesto o Año común, según el valor ingresado.

# Sería bueno verificar si el año ingresado cae en la era gregoriana y emitir una advertencia de lo contrario: 
# No dentro del período del calendario gregoriano. Consejo: utiliza los operadores != y %.

# Prueba tu código con los datos que hemos proporcionado.

# Datos de prueba:
# Entrada de muestra: 2000
# Resultado esperado: Año bisiesto

# Entrada de muestra: 2015
# Resultado esperado: Año común 

# Entrada de muestra: 1999
# Resultado esperado: Año común 

# Entrada de muestra: 1996
# Resultado esperado: Año bisiesto 

# Entrada de muestra: 1580
# Resultado esperado: No dentro del período del calendario gregoriano

# SOLUCIÓN:
año = int(input("Introduzca un año:"))

while año != 0:
    if(año > 1582):
        # Validando que el año sea aplicable el calendario gregoriano que se aplico en 1582
        # Si el año ingresado es mayor al año cuando se aplico el calendario, entonces que haga lo siguiente:
        if (año % 4 != 0):
            print("Año común")
        elif (año % 100 != 0):
            print("Año bisiesto")
        elif (año % 400 != 0):
            print("Año comun")
        else:
            print("Año bisiesto")
        # Si el año es menor a 1582 entonces: 
    else:
        print("No dentro del período del calendario gregoriano")
    año = int(input("Introduzca un año o Oprime 0 para finalizar:"))
print("Fin del programa...")


    




