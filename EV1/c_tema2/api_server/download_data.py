import requests, os

path_base = os.path.dirname(os.path.abspath(__file__))
URL_BASE = 'https://jsonplaceholder.typicode.com/'

endpoints = ['posts', 'comments', 'users']

for endpoint in endpoints:
	r = requests.get(f'{URL_BASE}{endpoint}')
	with open(f'{path_base}/data/{endpoint}.json', 'w', encoding='UTF-8') as file:
		file.write(r.text)
