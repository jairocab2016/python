# importamos el módulo
import subprocess

# Creamos los descriptores de archivos como dos vulgares archivos
# con permisos de escritura llamados 'archivo_out' y 'archivo_err'
outfd = open('archivo_out', 'w+')
errfd = open('archivo_err', 'w+')

# Supongamos que queremos ejecutamos el comando: ls -l -a
subprocess.call(['ls', '-l', '-a'], stdout=outfd, stderr=errfd)

# Cerramos los archivos para que se escriban los cambios y se liberen
# los buffers de I/O
outfd.close()
errfd.close()

# Ahora leemos todo lo que tengan los archivos y guardamos en la variable
# output la salida estándar y en err la salida de error.
fd = open('archivo_out', 'r')
output = fd.read()
fd.close()

fd = open('archivo_err', 'r')
err = fd.read()
fd.close()

# Por último mostramos lo que tienen las variables
print 'stdout: %s\n' % output
print 'stderr: %s' % err
