import requests
import json

if __name__ == '__main__':
	url = 'http://httpbin.org/post'
	payload = { 'nombre': 'Jairo', 'curso': 'python', 'nivel' : 'intermedio' }
	headers = {'Conten-Type': 'application/json', 'acces-toke': '12345'}

	response = requests.post(url, data=json.dumps(payload), headers=headers)

	#json post se encarga de serializarlos
	#data entonces nosotros nos encargamos de serializarlos
	print(response.url)

	if response.status_code == 200:
		#print(response.content)
		headers_response = response.headers #Dic
		print(headers_response)
		server = headers_response['Server']
		print(server)
