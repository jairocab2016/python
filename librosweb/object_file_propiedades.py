archivo = open("remeras.txt", "r+")
contenido = archivo.read()
nombre = archivo.name
modo = archivo.mode
encoding = archivo.encoding
archivo.close()

if archivo.closed:
    print "El archivo se ha cerrado correctamente"
else:
    print "El archivo permanece abierto"
print nombre
print modo
print encoding

# Cerrando archivos de forma automatica
with open("remeras.txt", "r") as archivo:
    contenido = archivo.read()

print archivo.closed
# True
