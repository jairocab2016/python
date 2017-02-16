# -*- coding: utf-8 -*-

# metodos de union y division

formato_numero_factura = ("Nº 0000-0", "-0000 (ID: ", ")")
numero = "275"
numero_factura = numero.join(formato_numero_factura)
print numero_factura

tupla = "http://www.eugeniabahit.com".partition("www.")

print tupla

protocolo, separador, dominio = tupla

print "Protocolo: {0}\nDominio: {1}".format(protocolo, dominio)


keywords = "python, guia, curso, tutorial".split(", ")

print keywords

texto = """Linea 1
Linea 2
Linea 3
Linea 4
"""
print texto.splitlines()

texto = "Linea 1\nLinea 2\nLinea 3"

print texto.splitlines()
