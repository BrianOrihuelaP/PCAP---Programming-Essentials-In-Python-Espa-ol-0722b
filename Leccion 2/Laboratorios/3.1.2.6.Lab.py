# CICLO FOR *****************************

# Escenario
# ¿Sabes lo que es Mississippi? Bueno, es el nombre de uno de los estados y ríos en los Estados Unidos. El río Mississippi tiene aproximadamente 2,340 
# millas de largo, lo que lo convierte en el segundo río más largo de los Estados Unidos (el más largo es el río Missouri). 
# ¡Es tan largo que una sola gota de agua necesita 90 días para recorrer toda su longitud!

# La palabra Mississippi también se usa para un propósito ligeramente diferente: para contar mississippily (mississippimente).

# Si no estás familiarizado con la frase, estamos aquí para explicarte lo que significa: se utiliza para contar segundos.

# La idea detrás de esto es que agregar la palabra Mississippi a un número al contar los segundos en voz alta hace que suene más cercano al reloj, 
# y por lo tanto "un Mississippi, dos Mississippi, tres Mississippi" tomará aproximadamente unos tres segundos reales de tiempo. A menudo lo usan los niños 
# que juegan al escondite para asegurarse de que el buscador haga un conteo honesto.


# Tu tarea es muy simple aquí: escribe un programa que use un ciclo for para "contar de forma mississippi" hasta cinco. Habiendo contado hasta cinco, 
# el programa debería imprimir en la pantalla el mensaje final "¡Listo o no, ahí voy!"

# SOLUCION:  
import time

    # Escribe un ciclo for que cuente hasta cinco.
for i in range(1, 6):
    print(i, "Mississippi")
    time.sleep(1)
    # Cuerpo del ciclo: imprime el número de iteración del ciclo y la palabra "Mississippi".
    # Cuerpo del ciclo - uso: time.sleep (1)
    # la funcion time.sleep pausa por un segundo al ciclo

# Escribe una función de impresión con el mensaje final.
print("¡Listo o no, ahí voy!!!")

#EXTRA: Pedir al usuario hasta que numero contar 
limite = int(input("Hasta que missisipi quieres contar?: "))

for i in range(1, limite + 1):
    print(i, "Mississippi")
    time.sleep(1)
    
print("¡Listo o no, ahí voy!!!")

