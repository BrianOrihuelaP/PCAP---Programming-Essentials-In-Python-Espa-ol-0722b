# Escenario
# Millas y kilómetros son unidades de longitud o distancia.

# Teniendo en mente que 1 equivale aproximadamente a 1.61 kilómetros, complemente el programa en el
# editor para que convierta de:

# Millas a kilómetros.
# Kilómetros a millas.

# No se debe cambiar el código existente. Escribe tu código en los lugares indicados con #.
# Prueba tu programa con los datos que han sido provistos en el código fuente.

kilometros = 12.25
millas = 7.38

# completar
millas_a_kilometros = 7.38 * 1.61
# completar
kilometros_a_millas = 12.25 / 1.61

print(millas, " millas son ", round(millas_a_kilometros, 2), " kilómetros ")
print(kilometros, " kilómetros son ", round(kilometros_a_millas, 2), " millas ")

# **Experimenta más ...............................................................................s
# Intenta escribir diferentes convertidores, por ejemplo, un convertidor de USD a EUR,un convertidor de temperatura, etc

# Conversion de dolares a pesos mex.
print("Conversor de pesos mex a dolares USA ++++++++++++++++++++++++++++++++++++")
dolaresUSA = 122.5
pesosMex = 1255.32

pesosMex_a_dolaresUSA = pesosMex / 20.37
dolaresUSA_a_pesosMex = dolaresUSA * 20.37

print(dolaresUSA, "dolares americanos son ", round(
    dolaresUSA_a_pesosMex, 2), " pesos mexicanos")
print(pesosMex, " pesos mexicanos son ", round(
    pesosMex_a_dolaresUSA, 2), "dolares americanos")

# Conversion de grados °C a °F
print("Conversor de grados °C a °F ++++++++++++++++++++++++++++++++++++")
gradosC = 36
gradosF = 144

gradosC_a_gradosF = (gradosC * 9/5) + 32
gradosF_a_gradosC = (gradosF - 32) * (5/9)

print(gradosC,"grados Celcius son ", gradosC_a_gradosF, "grados Farenheit")
print(gradosF, "grados Farenheit son ", round(gradosF_a_gradosC, 4), "grados Celcius")


