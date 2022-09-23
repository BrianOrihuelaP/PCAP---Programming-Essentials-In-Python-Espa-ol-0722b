# Brian Ulises Orihuela Perez --> 01/08/2022

# 2. Condicionales

# IF ******************************************************************************

# La primera forma de una declaración condicional, que puede ver a continuación, está escrita de manera muy
# informal pero figurada:

# if cierto_o_no:
#     hacer_esto_si_cierto

# Declaración del if:
# La palabra en si misma.

# Uno o más espacios en blanco.

# Una expresión (una pregunta o una respuesta) cuyo valor se interpretar únicamente en términos de True
# (cuando su valor no sea cero) y False (cuando sea igual a cero).

# Unos dos puntos seguido de una nueva línea.

# Una instrucción con sangría o un conjunto de instrucciones (se requiere absolutamente al menos una instrucción);
# la sangría se puede lograr de dos maneras: insertando un número particular de espacios (la recomendación es
# usar cuatro espacios de sangría), o usando el tabulador; nota: si hay mas de una instrucción en la parte con
# sangría, la sangría debe ser la misma en todas las líneas; aunque puede parecer lo mismo si se mezclan
# tabuladores con espacios, es importante que todas las sangrías sean exactamente iguales Python 3 no permite
# mezclar espacios y tabuladores para la sangría.

# Ejemplo:

print("Comprar sopa de 10 pesos")
dinero = float(input("¿Cuánto dinero tienes?: "))
if dinero >= 10:
    print("Compra botana")
print("Compra la sopa")

# En el ejemplo anterior se debe de "comprar" x producto, por ejemplo, nuestro producto tiene un precio de $10
# Así que dependiendo de nuestra entrada "dinero", el condicional if nos permitira comprar o no algo extra
# si tenemos más de $10 damos por hecho que nos podemos comprar x producto más de la tienda
# si solo tenemos los 10 exactos, entonces solo podemos comprar el producto que debemos de obtener

# Si observamos bien, que pasa si tenemos menos de $10?
# Exacto, aquí hay un error que más adelante resolveremos...

# IF & ELSE +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#Python nos permite expresar dichos planes alternativos. Esto se hace con una segunda forma, ligeramente mas 
# compleja, de la declaración condicional, la declaración if-else :

# if condición_true_or_false:
#     ejecuta_si_condición_true
#  else: 
#     ejecuta_si_condición_false 

# La ejecución de if-else es la siguiente:

# Si la condición se evalúa como Verdadero (su valor no es igual a cero), la instrucción ejecuta_si_condición_true se ejecuta, y la declaración condicional llega a su fin.
# Si la condición se evalúa como Falso (es igual a cero), la instrucción ejecuta_si_condición_false se ejecuta, y la declaración condicional llega a su fin.

# EJEMPLO:
print("IF & ELSE")
if dinero >= 10:
    print("Compra la sopa; " + "Puedes comprar algo extra :) ")
else:
    print("No te alcanza :(")
# Cómo se puede observar, hemos corregido el error anterior del ejemplo

# IF & ELSE ANIDADOS ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Otra caracteristica importante del if & else es que nos permite agregar dicha expresion dentro de su flujo
# de trabajo como se observa a continuación: 

print("IF & ELSE ANIDADOS")
if dinero >= 10:
    if dinero > 10:
        print("Compra la sopa; " + "Puedes comprar algo extra :) ")
    else:
        print("Solo puedes comprar la sopa :(")
else:
    print("No te alcanza :(")

# Como se puede apreciar en el ejemplo anterior, además de haber corregido el problema de inicio, ahora con una 
# anidación podemos saber si se tiene el dinero exacto y así hacer nuestro código un poco mas complejo

# ELIF ************************************************************************************************

# La declaración elif
# El segundo caso especial presenta otra nueva palabra clave de Python: elif. Como probablemente sospechas, 
# es una forma más corta de else-if.

# elif se usa para verificar más de una condición, y para detener cuando se encuentra la primera declaración 
# verdadera.

print("ELIF")
if dinero == 10:
    print("Solo puedes comprar la sopa :(")
elif dinero >= 10:
    print("Compra la sopa; " + "Puedes comprar algo extra :) ")
elif dinero < 10:
    print("Ups no te alcanza para la sopa :(")
else:
    print("No se compró nada :O")

# El uso de elif como se muestra nos puede ayudar a simplificar la anidación de if y else.

# Ejemplos 3.1.1.15
print("Uso de if else")
x = 10

if x == 10:
    print(x == 10) #True
if x > 5:
    print(x > 5) #True
if x < 10:
    print(x < 10) #---
else:
    print("else") # else

x = "1"

if x == 1:
    print("uno")
elif x == "1":
    if int (x)> 1:
        print("dos")
    elif int (x) < 1:
        print("tres")
    else:
        print("cuatro")
if int (x) == 1:
    print("cinco")
else:
    print("seis") 

# RESULTADO : CUATRO, CINCO

print("*********")
x = 1
y = 1.0
z = "1"

if x == y:
    print("uno")
if y == int (z):
    print("dos")
elif x == y:
    print("tres")
else:
    print("cuatro") 

# Resultado : uno, dos
# No entra al elif x == y dado que entro al if anterior