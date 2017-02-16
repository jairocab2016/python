
diccionario = {"color": "violeta", "talle": "XS", "precio": 174.25}
print diccionario

# Vaciar un diccionario
# diccionario.clear()
print diccionario
# Copiar un diccionario

remera = diccionario.copy()

print diccionario
print remera

diccionario.clear()
print diccionario
print remera

musculosa = remera
print remera
print musculosa

remera.clear()
print remera
print musculosa


# Crear un nuevo diccionario desde las claves de una secuencia
secuencia = ["color", "talle", "marca"]
diccionario1 = dict.fromkeys(secuencia)
print diccionario1

diccionario2 = dict.fromkeys(secuencia, 'valor x defecto')
print diccionario2


# Concatenar diccionarios
diccionario1 = {"color": "verde", "precio": 45}
diccionario2 = {"talle": "M", "marca": "Lacoste"}
diccionario1.update(diccionario2)
print diccionario1


# Establecer una clave y valor por defecto
remera = {"color": "rosa", "marca": "Zara"}
clave = remera.setdefault("talle", "U")
print clave
print remera

remera2 = remera.copy()
print remera2

clave = remera2.setdefault("estampado")
print clave

print remera2

clave = remera2.setdefault("marca", "Lacoste")
print clave

print remera2
