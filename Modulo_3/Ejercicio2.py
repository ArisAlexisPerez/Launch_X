# Si un asteroide entra en la atmósfera de la Tierra a una velocidad mayor o igual a 20 km/s, 
# a veces produce un rayo de luz que se puede ver desde la Tierra. 
# Escribe la lógica condicional que usa declaraciones if, else, y elif para alertar a las personas de todo el mundo 
# que deben buscar un asteroide en el cielo. 
# ¡Hay uno que se dirige a la tierra ahora a una velocidad de 19 km/s!

# Agrega el código para crear una variable para un asteroide que viaja a 19 km/s
# Escribe varias expresiones de prueba para determinar si puedes ver el rayo de luz desde la tierra
# Agrega las instrucciones que se ejecutarán si las expresiones de prueba son True o False

velocidad_asteroide = 19

if velocidad_asteroide > 25:
    print("¡Advertencia!... Un asteroide se acerca demasiado rápido a la tierra a " + str(velocidad_asteroide) + " km/s")
elif velocidad_asteroide >= 20:
     print("¡Asteroide Visible!... El rayo de luz del asteroide es visible desde la tierra.")
else:
    print("¡No hay visibilidad!... El asteroide viaja a una velocidad menor a 20 km/s.")

