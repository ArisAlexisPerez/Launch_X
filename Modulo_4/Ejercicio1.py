text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""
# Primero, divide el texto en cada oración para trabajar con su contenido:
# Añade el código necesario
text_en_oraciones = text.split('. ')
print(text_en_oraciones)

print('\n### Oraciones ###\n')

# Ahora, define algunas palabras clave para búsqueda que te ayudarán a determinar si una oración contiene un hecho.
# Define las palabras pista: average, temperature y distance suenan bien
palabras_clave = ['average', 'temperature', 'distance', 'satellite']

# Crea un bucle para imprimir solo datos sobre la Luna que estén relacionados con las palabras clave definidas anteriormente:
# Ciclo for para recorrer la cadena

for teo in text_en_oraciones:
    for pc in palabras_clave:
        if pc in teo:
            print('- ' + teo)
            break

print('\n### Remplazo a Celcius ###\n')

# Finalmente, actualiza el bucle(ciclo) para cambiar C a Celsius:
# Ciclo para cambiar C a Celsius
for teo in text_en_oraciones:
    for pc in palabras_clave:
        if pc in teo:
            print('- ' + teo.replace(' C', ' Celsius'))
            break
