## El while y la opción else

# Ambos ciclos, while y for, tienen una característica interesante (y rara vez se usa).
# Te mostraremos cómo funciona: intenta juzgar por ti mismo si es utilizable.
# En otras palabras, trata de convencerte si la función es valiosa y útil, o solo es azúcar sintáctica.

# Echa un vistazo al fragmento en el editor. Hay algo extraño al final: la palabra clave else.
# Como pudiste haber sospechado, los ciclos también pueden tener la rama else, como los if.
# La rama else del ciclo siempre se ejecuta una vez, independientemente de si el ciclo ha entrado o no en su cuerpo .

# ¿Puedes adivinar la salida? Ejecuta el programa para comprobar si tenías razón.
# Modifica el fragmento un poco para que el ciclo no tenga oportunidad de ejecutar su cuerpo ni una sola vez:

i = 1
while i < 5:
    #Ejecuta mientras i sea menor a 5 ( 1 - 4)
    print (i)
    #imprimimos el valor de i
    i += 1
    #aumentamos i para que sea ciclo, si no se hace infinito
else:
    #Despues de que se rompe el while entonces imprimimos esto
    print("Else:", i)


# Modifica el fragmento un poco para que el ciclo no tenga oportunidad de ejecutar su cuerpo ni una sola vez:
i = 5
while i < 5:
    print(i)
    i += 1
else:
    print("Else 2:", i)

# El estado de while es Falso al principio, ¿puedes verlo?
# Ejecuta y prueba el programa, y verifica si se ha ejecutado o no la rama else.

# El ciclo for y la rama else --------------------------------------------------------------------------------------------

# Los ciclos for se comportan de manera un poco diferente: echa un vistazo al fragmento en el editor y ejecútalo.
# La salida puede ser un poco sorprendente.
# La variable i conserva su último valor.


# Modifica el código un poco para realizar un experimento más.

i = 111
for i in range(2, 1): #nunca va a ejecutarse el for dado que su rango de inicio es irracional
    #for (inicio, para, paso)
    print(i)
else:
    #imprime el valor global de i
    print("else:", i) 

# ¿Puedes adivinar la salida?

# El cuerpo del ciclo no se ejecutará aquí en absoluto. Nota: hemos asignado la variable i antes del ciclo.
# Ejecuta el programa y verifica su salida.

# Cuando el cuerpo del ciclo no se ejecuta, la variable de control conserva el valor que tenía antes del ciclo.
# Nota: si la variable de control no existe antes de que comience el ciclo, no existirá cuando la ejecución llegue a la rama else.
# ¿Cómo te sientes acerca de esta variante de else?