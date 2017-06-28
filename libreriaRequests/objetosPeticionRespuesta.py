import requests

r = requests.get('http://en.wikipedia.org/wiki/Monty_Python')
print r.headers #acceder a las cabeceras que el servidor envio de vuelta
print ("-------------------")
print r.request.headers #obtener las cabeceras que enviamos al servidor
