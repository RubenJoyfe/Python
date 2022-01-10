import json, requests, sys, importlib

if len(sys.argv) != 2:
	print('Uso: python3 test.py <NombreApellidoApellido>')
	exit(-1)

try:
	examen = importlib.import_module(sys.argv[1])
except Exception:
	print('Error - Pasa como argumento el nombre de tu archivo python sin la extensión .py')
	exit(-1)

BASE_URL = 'http://127.0.0.1:5000/'

def check_result_1_a_1():
	try:
		result = examen.ejercicio1()
		return result == 4
	except Exception:
		return False

def check_result_1_a_2():
	try:
		result = examen.ejercicio2()
		return result == 'ruben@alummno.iepgroup.es'
	except Exception:
		return False

def check_result_1_a_3():
	try:
		examen.ejercicio3()
		posts = requests.get(f'{BASE_URL}posts').json()
		ids = [p['userId'] for p in posts]
		return ids == [102, 101, 102, 103]
	except Exception:
		return False

def check_result_1_a_4():
	try:
		examen.ejercicio4()
		posts = requests.get(f'{BASE_URL}posts').json()
		ids = [p['id'] for p in posts]
		return ids == [2, 6, 4]
	except Exception:
		return False

def check_result_1_a_5():
	try:
		comment_id = examen.ejercicio5()
		comment = requests.get(f'{BASE_URL}comments/{comment_id}').json()
		return comment['postId'] == 2
	except Exception:
		return False

def check_result_2_a_1():
	try:
		result = examen.ejercicio1()
		return result == 3
	except Exception:
		return False

def check_result_2_a_2():
	try:
		result = examen.ejercicio2()
		return result == 'Hayden@althea.biz'
	except Exception:
		return False

def check_result_2_a_3():
	try:
		examen.ejercicio3()
		posts = requests.get(f'{BASE_URL}posts').json()
		ids = [p['userId'] for p in posts]
		return ids == [102, 102, 103, 103]
	except Exception:
		return False

def check_result_2_a_4():
	try:
		examen.ejercicio4()
		posts = requests.get(f'{BASE_URL}posts').json()
		ids = [p['id'] for p in posts]
		return ids == [2, 8]
	except Exception:
		return False

def check_result_2_a_5():
	try:
		comment_id = examen.ejercicio5()
		comment = requests.get(f'{BASE_URL}comments/{comment_id}').json()
		return comment['postId'] == 1
	except Exception:
		return False

def check_result_1_b_1():
	try:
		result = examen.ejercicio1()
		return result == 3
	except Exception:
		return False

def check_result_1_b_2():
	try:
		result = examen.ejercicio2()
		return result == 4
	except Exception:
		return False

def check_result_1_b_3():
	try:
		examen.ejercicio3()
		comments = requests.get(f'{BASE_URL}comments').json()
		for comment in comments:
			if not comment['name'].endswith(' (Examen)'):
				return False
		return True
	except Exception:
		return False

def check_result_1_b_4():
	try:
		examen.ejercicio4()
		comments = requests.get(f'{BASE_URL}comments').json()
		ids = [c['id'] for c in comments]
		return ids == [1, 3, 4, 5, 6]
	except Exception:
		return False

def check_result_1_b_5():
	try:
		comment_id = examen.ejercicio5()
		comment = requests.get(f'{BASE_URL}comments/{comment_id}').json()
		return comment['postId'] == 6
	except Exception:
		return False

def check_result_2_b_1():
	try:
		result = examen.ejercicio1()
		return result == 2
	except Exception:
		return False

def check_result_2_b_2():
	try:
		result = examen.ejercicio2()
		return result == 2
	except Exception:
		return False

def check_result_2_b_3():
	try:
		examen.ejercicio3()
		comments = requests.get(f'{BASE_URL}comments').json()
		for comment in comments:
			if not comment['name'].endswith(' (Examen)'):
				return False
		return True
	except Exception:
		return False

def check_result_2_b_4():
	try:
		examen.ejercicio4()
		comments = requests.get(f'{BASE_URL}comments').json()
		ids = [c['id'] for c in comments]
		return ids == [1, 3, 4, 5]
	except Exception:
		return False

def check_result_2_b_5():
	try:
		comment_id = examen.ejercicio5()
		comment = requests.get(f'{BASE_URL}comments/{comment_id}').json()
		return comment['postId'] == 8
	except Exception:
		return False

def check_result_1_c_1():
	try:
		result = examen.ejercicio1()
		return result == 6
	except Exception:
		return False

def check_result_1_c_2():
	try:
		result = examen.ejercicio2()
		return result == 3
	except Exception:
		return False

def check_result_1_c_3():
	try:
		examen.ejercicio3()
		comments = requests.get(f'{BASE_URL}comments').json()
		for comment in comments:
			if not comment['name'].startswith('(Examen) '):
				return False
		return True
	except Exception:
		return False

def check_result_1_c_4():
	try:
		examen.ejercicio4()
		comments = requests.get(f'{BASE_URL}comments').json()
		ids = [c['id'] for c in comments]
		return ids == [2, 3, 4, 5, 6]
	except Exception:
		return False

def check_result_1_c_5():
	try:
		comment_id = examen.ejercicio5()
		comment = requests.get(f'{BASE_URL}comments/{comment_id}').json()
		return comment['postId'] == 6
	except Exception:
		return False

def check_result_2_c_1():
	try:
		result = examen.ejercicio1()
		return result == 5
	except Exception:
		return False

def check_result_2_c_2():
	try:
		result = examen.ejercicio2()
		return result == 2
	except Exception:
		return False

def check_result_2_c_3():
	try:
		examen.ejercicio3()
		comments = requests.get(f'{BASE_URL}comments').json()
		for comment in comments:
			if not comment['name'].startswith('(Examen) '):
				return False
		return True
	except Exception:
		return False

def check_result_2_c_4():
	try:
		examen.ejercicio4()
		comments = requests.get(f'{BASE_URL}comments').json()
		ids = [c['id'] for c in comments]
		return ids == [2, 4, 5, 6]
	except Exception:
		return False

def check_result_2_c_5():
	try:
		comment_id = examen.ejercicio5()
		comment = requests.get(f'{BASE_URL}comments/{comment_id}').json()
		return comment['postId'] == 8
	except Exception:
		return False

checks1 = {
	'a': {
		1: check_result_1_a_1,
		2: check_result_1_a_2,
		3: check_result_1_a_3,
		4: check_result_1_a_4,
		5: check_result_1_a_5
	},
	'b': {
		1: check_result_1_b_1,
		2: check_result_1_b_2,
		3: check_result_1_b_3,
		4: check_result_1_b_4,
		5: check_result_1_b_5
	},
	'c': {
		1: check_result_1_c_1,
		2: check_result_1_c_2,
		3: check_result_1_c_3,
		4: check_result_1_c_4,
		5: check_result_1_c_5
	}
}

checks2 = {
	'a': {
		1: check_result_2_a_1,
		2: check_result_2_a_2,
		3: check_result_2_a_3,
		4: check_result_2_a_4,
		5: check_result_2_a_5
	},
	'b': {
		1: check_result_2_b_1,
		2: check_result_2_b_2,
		3: check_result_2_b_3,
		4: check_result_2_b_4,
		5: check_result_2_b_5
	},
	'c': {
		1: check_result_2_c_1,
		2: check_result_2_c_2,
		3: check_result_2_c_3,
		4: check_result_2_c_4,
		5: check_result_2_c_5
	}
}

results = [False, False, False, False, False]

checks = checks1[examen.get_exam_version()]
for ejercicio in checks:
	examen.reset_data()
	results[ejercicio-1] = checks[ejercicio]()
checks = checks2[examen.get_exam_version()]
for ejercicio in checks:
	examen.reset_data('b')
	results[ejercicio-1] = results[ejercicio-1] and checks[ejercicio]()

for index, result in enumerate(results):
	print(f'Ejercicio {index+1} -----> {result}')
print(f'Puntuación: {results.count(True)*2}')

