import requests
import json

if __name__ == '__main__':
	url = 'http://httpbin.org/delete'
	payload = { 'nombre': 'Jairo', 'curso': 'python', 'nivel' : 'intermedio' }
	headers = {'Conten-Type': 'application/json', 'acces-toke': '12345'}

	response = requests.delete(url, data=json.dumps(payload), headers=headers)

	#GET para obtener algun recurso
	#POST para crearlo
	#PUT para actualizarlo
	#DELETE par eliminarlo
	print(response.url)

	if response.status_code == 200:
		#print(response.content)
		headers_response = response.headers #Dic
		server = headers_response['Server']
		print(server)
