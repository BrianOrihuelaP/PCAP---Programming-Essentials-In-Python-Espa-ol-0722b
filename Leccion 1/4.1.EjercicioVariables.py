#Resolviendo problemas matemáticos simples
#Ahora deberías de ser capaz de construir un corto programa el cual resuelva problemas matemáticos sencillos #como el Teorema de Pitágoras:

#El cuadrado de la hipotenusa es igual a la suma de los cuadrados de los dos catetos.

from math import sqrt
#Importando sqrt para el calculo de la raiz cuadrada

print("|Programa .- Teorema de Pitagoras|")
print("Introduce Cateto A: ")
catetoA = float(input())
print("Introduce Cateto B: ")
catetoB = float(input())
#Se hace casting a float dado que input retorna un string

print("Tus catetos son: ", catetoA, ";" , catetoB)

hipotenusa = (catetoA ** 2 + catetoB ** 2)

hipotenusa = sqrt(hipotenusa)

print("La hipotenusa del triangulo es: ", hipotenusa)