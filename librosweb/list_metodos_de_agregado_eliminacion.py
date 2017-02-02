

# agregar un elemento al final de la lista
nombres_masculinos = ["Alvaro", "Jacinto", "Miguel", "Edgardo", "David"]
nombres_masculinos.append("Jose")
print nombres_masculinos

# Agregar varios elementos al final de la lista
nombres_masculinos.extend(["Jose", "Gerardo"])
print nombres_masculinos

# Agregar un elemento en una posicion determinada
nombres_masculinos.insert(0, "Ricky")
print nombres_masculinos



# Eliminar el ultimo de la lista
nombres_masculinos.pop()
print nombres_masculinos

#Eliminar un elemento por su indice
nombres_masculinos.pop(3)
print nombres_masculinos

# Eliminar un elemento por su valor
nombres_masculinos.remove("Jose")
print nombres_masculinos