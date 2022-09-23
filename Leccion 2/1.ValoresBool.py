# Brian Ulises Orihuela Perez --> 01/08/2022

# 1. Valores Booleanos

# Una computadora ejecuta el programa y proporciona las respuestas.
# El programa debe ser capaz de reaccionar de acuerdo con las respuestas recibidas.
# Afortunadamente, las computadoras solo conocen dos tipos de respuestas:
# Si, es cierto.
# No, esto es falso.

# Comparación: operador de igualdad ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# El operador == (igual a) compara los valores de dos operandos. Si son iguales, el resultado de la comparación
#  es True. Si no son iguales, el resultado de la comparación es False.

# Observa la comparación de igualdad a continuación: ¿Cuál es el resultado de esta operación?
var = 0  # asignando 0 a var
print(var == 0)  # True

var = 1  # asignando 1 a var
print(var == 0)  # False

# Desigualdad: el operador no es igual a (!=)
# El operador != (no es igual a) también compara los valores de dos operandos. Aquí está la diferencia:
# si son iguales, el resultado de la comparación es False. Si no son iguales, el resultado de la comparación es True.
# Ahora echa un vistazo a la comparación de desigualdad a continuación: ¿Puedes adivinar el resultado de esta operación?

var = 0  # asignando 0 a var
print(var != 0)  # False

var = 1  # asignando 1 a var
print(var != 0)  # True

# Operadores de Comparación: Mayor que, Mayor o igual, Menor que, Menor o igual
# También se puede hacer una pregunta de comparación usando el operador > (mayor que).
# Si deseas saber si hay más ovejas negras que blancas, puedes escribirlo de la siguiente manera:

print("Comparando: ")
ovejasNegras = 8
ovejasBlancas = 10
print(ovejasNegras > ovejasBlancas)  # mayor que.
#R = False

ovejasNegras = 10
print(ovejasNegras >= ovejasBlancas)  # mayor o igual
#R = True

print(ovejasNegras <= ovejasBlancas)  # menor o igual
#R = True
# Se puede interpretar de dos maneras:
# 1.-ovejasBlancas son mayor o igual que...
# 2.-ovejasNegras son menor o igual que...

ovejasNegras = 20
print(ovejasNegras < ovejasBlancas ) # menor que
# R = False
