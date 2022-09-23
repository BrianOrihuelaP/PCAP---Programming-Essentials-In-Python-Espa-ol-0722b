# ESCENARIO 3

# La tarea es preparar un código simple para evaluar o encontrar el tiempo final de un periodo de tiempo dado, 
# expresándolo en horas y minutos. Las horas van de 0 a 23 y los minutos de 0 a 59. El resultado debe ser mostrado en la consola.
# Por ejemplo, si el evento comienza a las 12:17 y dura 59 minutos, terminará a las 13:16.

# Prueba el código cuidadosamente. Pista: utilizar el operador % puede ser clave para el éxito.

# Datos de Prueba
# Entrada de muestra:
# 12
# 17
# 59
# Salida esperada: 13:16

# Entrada de muestra:
# 23
# 58
# 642
# Salida esperada: 10:40

# Entrada de muestra:
# 0
# 1
# 2939
# Salida esperada: 1:0

# SOLUCIÓN:

hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# coloca tu código aqui
print("Tu inicio es a las: ",hora,":",min)
print("Tu actividad dura: ",dura)

horaFin = min + dura

#Como extra se uso un if else para que nos arroje correctamente la hora cuando una actividad pasa de los 60 mins
if horaFin < 60:
    print("Tu actividad termina a las: " + str(hora) + ":" + str(min + dura))
else:
    print("Tu actividad termina a las: " + str(hora + 1) + ":"+ str(horaFin - 60))


#FINAL: 
# ¿Cuál es la salida del siguiente código?
x = int(input("Ingresa un número: ")) #  el usuario ingresa un 2
print(x * "5")
# Salida : 22222

# ¿Cuál es la salida esperada del siguiente código?
x = input("Ingresa un número: ") # el usuario ingresa un 2
print(type(x)) #Salida: <class:'str'>

#type nos indica el tipo de variable




