# Para este ejercicio, escribirás una lógica condicional que imprima una advertencia si un asteroide 
# se acerca a la Tierra demasiado rápido. La velocidad del asteroide varía dependiendo de lo cerca que 
# esté del sol, y cualquier velocidad superior a 25 kilómetros por segundo (km/s) merece una advertencia.

# Añadir el código necesario para crear una variable que guarde la velocidad del asteroide.
# Escribe una expresión de prueba para calcular si necesita una advertencia.
# Agregue las instrucciones que se ejecutarán si la expresión de prueba es true o false.

velocidad_asteroide = 49

if velocidad_asteroide > 25:
    print("¡Advertencia!... Un asteroide se acerca demasiado rápido a la tierra a " + str(velocidad_asteroide) + " km/s")
else:
    print("¡Todo normal!... Puede continuar con su vida.")

