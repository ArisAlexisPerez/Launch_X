# Ejecutar un programa
# program.py
sum = 1 + 2
print(sum)

# La función print()
# Impresión en pantalla print('Hola desde la consola')
print('Hola desde la consola')

# Variables
sum = 1 + 2 # 3
product = sum * 2
print(product)

# Tipos de datos
# Númerico, Texto, Booleano
planetas_en_el_sistema_solar = 8 # int, plutón era considerado un planeta pero ya es muy pequeño
distancia_a_alfa_centauri = 4.367 # float, años luz
puede_despegar = True
transbordador_que_aterrizo_en_la_luna = "Apollo 11" # string 

# Declaramos la variable
distancia_a_alfa_centauri = 4.367

# Descubrimos su tipo de dato
print (type(distancia_a_alfa_centauri))

# Operadores
# <left side> <operator> <right side>
left_side = 10
right_side = 5
print(left_side / right_side) # 2

# Operadores aritméticos
# +	Operador de adición que suma dos valores juntos.
# -	Operador de resta que quita el valor del lado derecho del lado izquierdo.
# /	Operador de división que divide el lado izquierdo tantas veces como especifique el lado derecho.
# *	Operador de multiplicación.

# Operadores de asignación
# =	    x = 2
# +=	x += 2
# -=	x -= 2
# /=	x /= 2
# *=	x *= 2

# Fechas
# Para trabajar con una fecha, debe importar el módulo: from datetime import date
# Para obtener la fecha de hoy, puede llamar a la función: date.today()
from datetime import date
print(date.today())

# Conversión de tipos de datos
print("Today's date is: " + str(date.today()))

# Recopilar información
# Entrada del usuario
print("Bienvenido al programa de bienvenida")
name = input("Introduzca su nombre ")
print("Saludos: " + name)

# Trabajar con números
print("Calculadora")
first_number = input("Primer número: ")
second_number = input("Segundo número: ")
#print(first_number + second_number)
print(int(first_number) + int(second_number))

