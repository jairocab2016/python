import requests

if __name__ == '__main__':
	url = 'http://httpbin.org/get'
	args = { 'nombre': 'Jairo', 'curso': 'python', 'nivel' : 'intermedio' }
	response = requests.get(url, params = args)
	print(response.url)

	if response.status_code == 200:
		content = response.content
		print(content)


