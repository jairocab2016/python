

# Conversion de tipos
tupla = (1, 2, 3, 4)
print tupla

list= list(tupla)
print (list)

tupla= tuple(list)
print tupla

# Concatenacion simple de colecciones

lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6, 7, 8]
lista3 = lista1 + lista2
print lista3

tupla1 = (1, 2, 3, 4, 5)
tupla2 = (4, 6, 8, 10)
tupla3 = (3, 5, 7, 9)
tupla4 = tupla1 + tupla2 + tupla3
print tupla4

# Valor maximo y minimo

print max(tupla4)
print max(tupla1)

print min(tupla1)
print max(lista3)
print min(lista1)

# Contar elementos
print len(lista3)
print len(lista1)
print len(tupla2)
