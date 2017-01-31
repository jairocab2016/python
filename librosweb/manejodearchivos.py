# -*- coding: utf-8 -*-

# Abrimos el archivo codehero.txt
fo = open("codehero.txt", "wb")
fo.write( "Codehero es una gran pagina para aprender a programar Python.\nSíguenos en @codeheroblog!!\n");

# Cerramos el archivo codehero.txt
fo.close()





# Abrimos el archivo codehero.txt
fo = open("codehero.txt", "r+")
str = fo.read(10);
print "La lectura es : ", str

# Cerramos el archivo codehero.txt
fo.close()