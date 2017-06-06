# -*- coding: utf-8 -*-


def mi_funcion():
    print "Hola Mundo"

mi_funcion()


def funcion():
    return "Hola Mundo"

frase = funcion()
print frase


# Parámetros por omisión
def saludar(nombre, mensaje='Hola'):
    print mensaje, nombre

saludar('Pepe Grillo')  # Imprime: Hola Pepe Grillo


# Keywords como parámetros

def saludar(nombre, mensaje='Hola'):
    print mensaje, nombre

saludar(mensaje="Buen día", nombre="Juancho")

print "\n\n"

# Parámetros arbitrarios


def recorrer_parametros_arbitrarios(parametro_fijo, *arbitrarios):
    print parametro_fijo

    # Los parámetros arbitrarios se corren como tuplas
    for argumento in arbitrarios:
        print argumento

recorrer_parametros_arbitrarios(
    'Fixed', 'arbitrario 1', 'arbitrario 2', 'arbitrario 3')


print "\n\n"


# Es posible también, obtener parámetros arbitrarios como pares de
# clave=valor. En estos casos, al nombre del parámetro deben precederlo
# dos astericos (**):

def recorrer_parametros_arbitrarios(parametro_fijo, *arbitrarios, **kwords):
    print parametro_fijo
    for argumento in arbitrarios:
        print argumento

    # Los argumentos arbitrarios tipo clave, se recorren como los diccionarios
    for clave in kwords:
        print "El valor de", clave, "es", kwords[clave]

recorrer_parametros_arbitrarios("Fixed", "arbitrario 1", "arbitrario 2",
                                "arbitrario 3", clave1="valor uno", clave2="valor dos")


print "\n\n"


# Desempaquetado de parámetros
def calcular(importe, descuento):
    return importe - (importe * descuento / 100)

datos = [1500, 10]
print calcular(*datos)


print "\n\n"


# El mismo caso puede darse cuando los valores a ser pasados como parámetros a una función, se encuentren disponibles en un diccionario.
# Aquí, deberán pasarse a la función, precedidos de dos asteriscos (**):
def calcular(importe, descuento):
    return importe - (importe * descuento / 100)

datos = {"descuento": 10, "importe": 1500}
print calcular(**datos)
