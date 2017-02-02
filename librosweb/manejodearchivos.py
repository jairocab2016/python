# -*- coding: utf-8 -*-

# Abrimos el archivo remeras.txt
fo = open("remeras.txt", "wb")
fo.write( "Codehero es una gran pagina para aprender a programar Python.\nSíguenos en @codeheroblog!!\n");

# Cerramos el archivo remeras.txt
fo.close()





# Abrimos el archivo remeras.txt
fo = open("remeras.txt", "r+")
str = fo.read(10)
print "La lectura es : ", str

# Cerramos el archivo remeras.txt
fo.close()