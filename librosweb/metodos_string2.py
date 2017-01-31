
#metodos de susticion

cadena = "bienvenido a mi aplicacion {0}"
print cadena.format("en Python")

cadena1 = "Importe bruto: ${0} + IVA: ${1} = Importe neto: {2}" 
print cadena1.format(100, 21, 121)

cadena2 = "Importe bruto: ${bruto} + IVA: ${iva} = Importe neto: {neto}"
print cadena2.format(bruto=100, iva=21, neto=121)

print cadena2.format(bruto=100, iva=100 * 21 / 100, neto=100 * 21 / 100 + 100)


buscar = "nombre apellido" 
reemplazar_por = "Juan Perez"

print "Estimado Sr. nombre apellido:".replace(buscar, reemplazar_por)

cadena3 = "   www.eugeniabahit.com   "
print cadena3.strip()

print cadena3.lstrip("w." )

print cadena3.lstrip()

print cadena3.rstrip()

