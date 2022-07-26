# Literales en python-----------
print("2")  # cadena
print(2)  # literal entera
print(1_111_111)  # literal con _ para una mejor comprensenion del numero
# utilizando el sistema octal:
print(0o123)
# python hace la conversion automaticamente al igual que en hexadecimal
print(0x123)
# numero flotante
print("Soy un flotante: ", 4.23)
print("Exponencial e: ", 3e10)
print("Soy la constante de planck (h): ", 6.62607e-34)
print("Python me muestra numeros pequeños en notacion cientifica: ",
      0.0000000000000000000001)
# escape \\ para usar comillas dobles o simples
print("Hola soy \"Guido Van Rossum\"")
print('I\'m Monty Python.')
# usando comillas simples para esto:
print('Hola soy "Guido Van Rossum"')
# valores booleanos
print(True > False)
print(True < False)

# Problema:
# Escribe una sola línea de código, utilizando la función print(), así como los caracteres de nueva línea 
# y escape, para obtener la salida esperada de tres líneas.

#Salida Esperada:------------------------------------------
# "Estoy"
# ""aprendiendo""
# """Python"""
#----------------------------------------------------------

#SOLUCION: 
print('"Estoy"\n""Aprendiendo""\n"""Python"""')