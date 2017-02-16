
# Obtener el valor de una clave
remera = {"color": "rosa", "marca": "Zara"}
print remera.get("color")

# Saber si una clave existe en el diccionario
existe = remera.has_key("precio")
print existe

existe = remera.has_key("color")
print existe

# Obtener las claves y valores de una diccionario
diccionario = {'color': 'rosa', 'marca': 'Zara', 'talle': 'U'}

for clave, valor in diccionario.iteritems():
    print "El valor de la clave %s es %s" % (clave, valor)

# Obtener las claves de un diccionario
diccionario = {'color': 'rosa', 'marca': 'Zara', 'talle': 'U'}
claves = diccionario.keys()
print claves

# Obtener los valores de un diccionario
valores = diccionario.values()
print valores

# Obtener la cantidad de elementos de un diccionario
print len(diccionario)
