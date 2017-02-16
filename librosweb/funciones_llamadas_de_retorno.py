# -*- coding: utf-8 -*-
"""
def mi_funcion():
    return "Hola Mundo" 
 
def saludar(nombre, mensaje='Hola'): 
    print mensaje, nombre 
    print mi_funcion()

saludar("jairo") """


# def funcion():
#     return "Hola Mundo"


# """Llamada de retorno a nivel global"""
# # def llamada_de_retorno(func):
# #    return globals()[func]()
# # print llamada_de_retorno("funcion")


# # Llamada de retorno a nivel local
# nombre_de_la_funcion = "funcion"
# print locals()[nombre_de_la_funcion]()


# def funcion(nombre):
#     return "Hola " + nombre

# def llamada_de_retorno(func=""):
#     """Llamada de retorno a nivel global"""
#     return globals()[func]("Laura")

# print llamada_de_retorno("funcion")

# # Llamada de retorno a nivel local
# nombre_de_la_funcion = "funcion"
# print locals()[nombre_de_la_funcion]("Facundo")


# if nombre_de_la_funcion in locals():
#     if callable(locals()[nombre_de_la_funcion]):
#         print locals()[nombre_de_la_funcion]("Emilse")


def funcion(nombre):
    return "Hola " + nombre


def llamada_de_retorno(func=""):
    if func in globals():
        if callable(globals()[func]):
            return globals()[func]("Laura")
    else:
        return "Función no encontrada"

print llamada_de_retorno("funcion")

nombre_de_la_funcion = "funcion"

if nombre_de_la_funcion in locals():
    if callable(locals()[nombre_de_la_funcion]):
        print locals()[nombre_de_la_funcion]("Facundo")
else:
    print "Función no encontrada"
