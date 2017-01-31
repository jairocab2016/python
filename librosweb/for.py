# lista=[12,31,23,12,312]

# for valor in lista:
# 	print "su valor  es " + str(valor)


# # Midiendo cadenas de texto
# palabras = ['gato', 'ventana', 'defenestrado']
# for p in palabras:
#      print "%s tiene %s letras" % (p, len(p))



for n in range(2, 10):
    for x in range(2, n):
    	if n % x == 0:
    		print(n, 'es igual a', x, '*', n/x)
         	break
    	else:
         # sigue el bucle sin encontrar un factor
         	print(n, 'es un numero primo')