
"""
Para calcular la serie fibonacci se va sumando cada resultado
teniendo que los dos primeros terminos son 0 y 1

n = 1: 0
n = 2: 1
n = 3: 1 -> 0 + 1
n = 4: 2 -> 1 + 1
n = 5: 3 -> 2 + 1
n = 6: 5 -> 3 + 2

"""

def fibo(x):
    # Primer termino = 0
    if x == 1:
        return 0
    # Segundo termino = 1
    elif x == 2:
        return 1
    else:
        return fibo(x - 1) + fibo(x - 2)

# Ejemplo para mostrar los terminos del 1 al 9
for i in range(1, 10):
    print 'n = %i: %i' % (i, fibo(i))