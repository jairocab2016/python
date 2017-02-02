import os
from subprocess import call
from subprocess import PIPE, Popen

# El modulo os y las variables de entorno
for variable, valor in os.environ.iteritems():
    print "%s: %s" % (variable, valor)

#Modulo subprocess
call('clear')
comando_y_argumentos = ['ls', '-lha']
call(comando_y_argumentos)

#Capturando la salida con Popen
proceso = Popen(['ls', '-lha'])
proceso.wait()

#Utilizando tuberias para capturar la salida
proceso = Popen(['ls', '-lha'], stdout=PIPE, stderr=PIPE)
error_encontrado = proceso.stderr.read()
proceso.stderr.close()
listado = proceso.stdout.read()
proceso.stdout.close()

if not error_encontrado:
    print listado
else:
    print "Se produjo el siguiente error:\n%s" % error_encontrado