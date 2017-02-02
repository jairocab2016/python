
#metodo seek
archivo = open("remeras.txt", "r")
contenido = archivo.read()
# el puntero queda
# al final del documento
archivo.seek(0)

#metodo read
archivo = open("remeras.txt", "r")
contenido = archivo.read()
print contenido

#metodo readline
archivo = open("remeras.txt", "r")
linea1 = archivo.readline()
print linea1

#metodo readlines
archivo = open("remeras.txt", "r")
for linea in archivo.readlines():
    print linea

print "-----------------------------------"
#metodo tell
archivo = open("remeras.txt", "r")
linea1 = archivo.readline()
mas = archivo.read(archivo.tell() * 2)

if archivo.tell() > 50:
    archivo.seek(50)

#metodo write
archivo = open("remeras.txt", "r+")
contenido = archivo.read()
final_de_archivo = archivo.tell()

archivo.write("Nueva linea")
archivo.seek(final_de_archivo)
nuevo_contenido = archivo.read()

print nuevo_contenido
# Nueva linea


# writelines(secuencia) Secuencia sera cualquier iterable cuyos elementos seran escritos uno por linea.

# archivo = open("remeras.txt", "r+")
# contenido = archivo.read()
# final_de_archivo = archivo.tell()
# lista = ['Linea 1\n', 'Linea 2']
#
# archivo.writelines(lista)
# archivo.seek(final_de_archivo)
#
# print archivo.readline()
# # Linea 1
#
# print archivo.readline()
# # Linea 2


#metodo close
archivo = open("remeras.txt", "r")
contenido = archivo.read()
archivo.close()
print contenido