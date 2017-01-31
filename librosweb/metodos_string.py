# -*- coding: utf-8 -*-

# metodos de formato
cadena = "bienvenido a mi aplicacion" 

print cadena.capitalize()

cadena1= "Hola mundo"
print cadena1.lower()

cadena2= "Hola Mundo"
print cadena2.upper()

print cadena2.swapcase()

print cadena1.title()

cadena = "Bienvenido a mi aplicacion".capitalize()

print cadena.center(50,"=")

print cadena.ljust(50, "=")

print cadena.rjust(50, "=")

numero_factura = 1575

print str(numero_factura).zfill(12)



# metodos de busqueda

print cadena.count("a")

print cadena.find("mi")

print cadena[13:15]

print cadena.find("mi", 0, 10)


#metodos de validacion

print cadena.startswith("Bienvenido")

print cadena.startswith("aplicación")

print cadena.startswith("aplicacion", 16)

print cadena.endswith("aplicacion")

print cadena.endswith("Bienvenido")

print cadena.endswith("Bienvenido", 0, 10)

cadena3= "pepegrillo 75"
print cadena3.isalnum()

cadena3=  cadena = "pepegrillo" 
print cadena3.isalnum()

print cadena3.isalpha()

cadena3= "123"
print cadena3.isdigit()


print cadena.islower()

print cadena.isupper()

cadena_vacia= " "
print cadena_vacia.isspace()

print cadena2.istitle() 