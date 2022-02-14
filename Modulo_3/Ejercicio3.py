# Los asteroides de menos de 25 metros en su dimensión más grande probablemente se quemarán a medida que entren
# en la atmósfera de la Tierra.
# Si una pieza de un asteroide que es más grande que 25 metros pero más pequeña que 1000 metros golpeara la Tierra, 
# causaría mucho daño. 
# También discutimos en el ejercicio anterior que:
# La velocidad del asteroide varía en función de lo cerca que esté del sol, y cualquier velocidad superior a 
# 25 kilómetros por segundo (km/s) merece una advertencia.
# Si un asteroide entra en la atmósfera de la Tierra a una velocidad mayor o igual a 20 km/s, a veces produce un rayo 
# de luz que se puede ver desde la Tierra.
# Usando toda esta información, escribe un programa que emita la advertencia o información correcta a la gente de la 
# Tierra, según la velocidad y el tamaño de un asteroide.

# Agrega el código para crear nuevas variables para la velocidad y el tamaño del asteroide
# Para probar el código, prueba con varias velocidades y tamaños
# Escribe varias expresiones de prueba o combinaciones de expresiones de prueba para determinar qué mensaje se debe enviar a Tierra.

velocidad_asteroide = 19
dimension = 24

if (velocidad_asteroide > 25) or (dimension >= 25 and dimension <1000 ):
    print("¡Advertencia!... Un asteroide se acerca la tierra a " + str(velocidad_asteroide) + " km/s" + " y su dimensión es de " + str(dimension) + " mts")
elif velocidad_asteroide >= 20:
     print("¡Asteroide Visible!... El rayo de luz del asteroide es visible desde la tierra.")
else:
    print("¡No hay visibilidad!... El asteroide viaja a una velocidad menor a 20 km/s o es menor a 25 mts.")





