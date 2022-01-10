import json, requests, os, webbrowser

from requests.api import request

path_base = os.path.dirname(os.path.abspath(__file__))
BASE_URL = 'https://jsonplaceholder.typicode.com/'

def searchUser(user_id):
    result = requests.get(f'{BASE_URL}users/{user_id}')
    user = result.json()
    return user

def saveResult(result, filename="posts", ind=4):
    with open(f'{path_base}/{filename}.json', 'w') as f:
        if type(result) == list:
            f.write(json.dumps(result, indent=ind))
        else:
            f.write(json.dumps(result.json(), indent=ind))

def postData(dt):
    return requests.post(f'{BASE_URL}posts', data=dt)

def putData(dt, post_id):
    return requests.put(f'{BASE_URL}posts/{post_id}', data=dt)

def deleteData(post_id):
    return requests.delete(f'{BASE_URL}posts/{post_id}')

result = requests.get(f'{BASE_URL}posts')

if (result.status_code!=200):
    exit(0)

data={
    "title": "adsa",
    "body": "adadadsadasda",
    "userId": 69
}

respuesta = postData(data)
respuesta = putData(data, 116)
respuesta = deleteData(169)

if (respuesta.status_code>=200 and respuesta.status_code<300):
    print(f'code: {respuesta.status_code}: {respuesta.json()}')
else:
    print(f'code: {respuesta.status_code}')

exit(0)

data = result.json()
user_id = data[0]['userId'] # print(json.dumps(data[0], indent=4))

print(searchUser(user_id)["name"])

saveResult(result, "posts", 4)
saveResult(requests.get(f'{BASE_URL}users'), "users", 4)

users = requests.get(f'{BASE_URL}users').json()

for usr in users:
    usr_posts = requests.get(f'{BASE_URL}posts/?userId={usr["id"]}')
    if (usr_posts.status_code==200):
        usr['posts'] = usr_posts.json()
        for upos in usr['posts']:
            upos.pop("userId", None)

saveResult(users, "usersPosts", 4)