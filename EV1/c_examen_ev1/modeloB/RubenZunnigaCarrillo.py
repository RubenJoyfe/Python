import requests, json, os

BASE_URL = 'http://127.0.0.1:5000/'
path_base = os.path.dirname(os.path.abspath(__file__))

def get_exam_version():
	# return 'a'
	return 'b'
	# return 'c'

def ejercicio1():
	posts = requests.get(f'{BASE_URL}posts').json()
	usersWithComents = []
	for post in posts:
		try:
			if usersWithComents.index(post['userId']):
				continue
		except Exception:
			usersWithComents.append(post['userId'])
	if len(usersWithComents) != 0:
		return len(usersWithComents)
	return None

def ejercicio2():
	search = 'Nice job, Jennifer!'
	posts = requests.get(f'{BASE_URL}posts').json()
	try:
		for post in posts:
			if search in post['body']:
				return post['id']
	except Exception:
		print("no hay body")
	return None

def ejercicio3():
	comments = requests.get(f'{BASE_URL}comments').json()
	data = {"id":1,"name":""}
	for com in comments:
		data['id']=com['id']
		data['name']=com['name']+" (Examen)"
		req = requests.put(f'{BASE_URL}comments/{com["id"]}', json=data)
	return

def ejercicio4():
	comments = requests.get(f'{BASE_URL}comments').json()
	try:
		for com in comments:
			if com['body'] == "":
				req = requests.delete(f'{BASE_URL}comments/{com["id"]}')
				# print(req.status_code)
	except Exception:
		print("no hay body")
	return

def getLastPostId():
	posts = requests.get(f'{BASE_URL}posts').json()
	id = 0
	for post in posts:
		if post['id']>id:
			id=post['id']
	return id

def ejercicio5():
	newcom = {}
	with open(f'{path_base}/new_comment.json', 'r') as f:
		newcom=json.loads(f.read())
	newcom['postId']=getLastPostId()
	req = requests.post(f'{BASE_URL}comments', json=newcom)
	if req.status_code > 200 or req.status_code < 300:
		return req.json()['id']
	return None

# No tocar
def reset_data(data = 'a'):
	requests.post(f'{BASE_URL}data/{data}')

def main():
	reset_data()
	print(ejercicio1())
	print(ejercicio2())
	print(ejercicio3())
	print(ejercicio4())
	print(ejercicio5())

# No tocar
if __name__ == "__main__":
	main()