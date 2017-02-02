import random


# Generar numeros aleatorios entre 49999 y 99999
lista = []

for n in range(0, 50):
    lista.append(random.randint(49999, 99999))

# Elegir un nuero al azar
numero_al_azar = random.choice(lista)

# Elegir 5 numeros al azar
numeros_al_azar = random.sample(lista, 5)

# reordenar los elementos de una lista
mujeres = ["Ana", "Beatriz", "Camila", "Carmen", "Delia", "Dora", "Emilse"]
random.shuffle(mujeres)
