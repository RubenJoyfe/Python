import json, requests, os, webbrowser

from requests.api import get, request

path_base = os.path.dirname(os.path.abspath(__file__))
BASE_URL = 'http://127.0.0.1:5000/'


#---------------------------------POSTS---------------------------------#

def searchPost(post_id):
    req = requests.get(f'{BASE_URL}posts/{post_id}')
    if req.status_code >= 200 and req.status_code < 300:
        return req.json()
    return req.status_code

def getData(post_id):
    req = requests.get(f'{BASE_URL}posts/{post_id}')
    if req.status_code >= 200 and req.status_code < 300:
        return req.json()
    return req.status_code
def getAllData():
    req =  requests.get(f'{BASE_URL}posts')
    if req.status_code >= 200 and req.status_code < 300:
        return req.json()
    return req.status_code

def postData(dt):
    req =  requests.post(f'{BASE_URL}posts', json=dt)
    if req.status_code >= 200 and req.status_code < 300:
        return req.json()
    return req.status_code
def putData(dt, post_id):
    req =  requests.put(f'{BASE_URL}posts/{post_id}', json=dt)
    if req.status_code >= 200 and req.status_code < 300:
        return req.json()
    return req.status_code

def deleteData(post_id):
    return requests.delete(f'{BASE_URL}posts/{post_id}').status_code


#---------------------------------COMMENTS---------------------------------#
def searchComment(comment_id):
    req =  requests.get(f'{BASE_URL}comments/{comment_id}')
    if req.status_code >= 200 and req.status_code < 300:
        return req.json()
    return req.status_code

def getComment(comment_id):
    req =  requests.get(f'{BASE_URL}comments/{comment_id}')
    if req.status_code >= 200 and req.status_code < 300:
        return req.json()
    return req.status_code
def getAllComments():
    req =  requests.get(f'{BASE_URL}comments')
    if req.status_code >= 200 and req.status_code < 300:
        return req.json()
    return req.status_code

def postComment(dt):
    req =  requests.post(f'{BASE_URL}comments', json=dt)
    if req.status_code >= 200 and req.status_code < 300:
        return req.json()
    return req.status_code

def putComment(dt, comment_id):
    req =  requests.put(f'{BASE_URL}comments/{comment_id}', json=dt)
    if req.status_code >= 200 and req.status_code < 300:
        return req.json()
    return req.status_code

def deleteComment(comment_id):
    return requests.delete(f'{BASE_URL}comments/{comment_id}').status_code

#---------------------------------GLOBAL_CODE---------------------------------#
postdata = {
    "userId": 1,
    "title": "Hola mundo",
    "body": "Mi nuevo post chupiguay",
}
putdata = {
    "userId": 69,
    "title": "MODIFICADO",
    "body": "https://c.tenor.com/hwdPpOWjOCQAAAAC/siuuuu-siiuu.gif, suuuuuu"
}

postcommentdata = {
    'body': "Reeeeequeson manteca y tum...",
    'email': "ruben@gmail.com",
    'name': "ruben",
    'postId': 100 
}

putcommentdata = {
    'email': "ruben@gmail.com",
    'name': "ruben",
    'body': "adre BELEN, campanas de BELEN"
}

def createPostpauseDeletePost(psdt):
    post = postData(psdt)
    respuesta = getData(post.json()['id'])
    print(respuesta.json())
    input()
    respuesta = deleteData(post.json()['id'])
    print(f'borrando post {post.json()["id"]}... code: {respuesta.status_code}')

def getNPosts():
    dataN=0
    for data in getAllData():
        dataN+=1
    return dataN

def getAllPostsOfUser(user_id):
    l = []
    for data in getAllData():
        if data['userId'] == user_id:
            l.append(data)
    return l

def idComentariosHuerfanos():
    ac = getAllData()
    found = False
    for coment in getAllComments():
        for post in ac:
            if coment['postId'] == post['id']:
                found = True
                break
            found = False
        if not found:
            print(f"Id comentario huerfano: {coment['id']}")

def eliminarComentariosSinPost():
    comentariosBorrados=[]
    ac = getAllData()
    found = False
    for coment in getAllComments():
        for post in ac:
            if coment['postId'] == post['id']:
                found = True
                break
            found = False
        if not found:
            comentariosBorrados.append(coment)
            print(deleteComment(coment['id']))
    
    return comentariosBorrados
    # print(comentariosBorrados)

def eliminarPostConComentarios(id_delete):
    print(deleteData(id_delete))
    allcom = getAllComments()
    for coment in allcom:
        if coment['postId'] == id_delete:
            print(deleteComment(coment['id']))

def guardarEnArchivo(data, titulo="save"):
    with open(f'{path_base}/{titulo}.json', 'w') as f:
        f.write(json.dumps(data, indent=4))


def guardarTodoDeUsuario(user_id, titulo=""):
    if titulo == "":
        titulo=f"user_{user_id}"

    allPosts  = []
    userPosts = getAllPostsOfUser(user_id)
    userComments = getAllComments()

    for post in userPosts:
        allpostComments = []
        for coment in userComments:
            if coment['postId'] == post['id']:
                cpcoment = coment.copy()
                cpcoment.pop('postId')
                allpostComments.append(cpcoment)
        post.pop('userId')
        post['comments'] = allpostComments
        allPosts.append(post)
    
    plantilla = {
        "userId": user_id,
        "posts": allPosts
    } 

    guardarEnArchivo(plantilla, titulo)



guardarTodoDeUsuario(6)

# idComentariosHuerfanos()
# eliminarComentariosSinPost()
# idComentariosHuerfanos()

# print(postComment(postcommentdata))
# print(putComment(putcommentdata, 500))

# eliminarPostConComentarios(100)

# print(json.dumps(getAllComment(), indent=4))


# print(len(getAllData()))

# Generar 5 comentarios pero los borro, no sin antes guardarlos en un archivo
# for x in range(0,5):
#     postComment(postcommentdata)

# guardarEnArchivo(eliminarComentariosSinPost(), "comentarios_sin_post")


# eliminarComentariosSinPost()
print("Soytontísimo")
exit(0)

createPostpauseDeletePost(postdata)

respuesta = putData(putdata, 104)
# respuesta = deleteData(169)

print(respuesta)


# if (respuesta.status_code>=200 and respuesta.status_code<300):
#     print(f'code: {respuesta.status_code}: {respuesta.json()}')
# else:
#     print(f'code: {respuesta.status_code}')


# def saveResult(result, filename="posts", ind=4):
#     with open(f'{path_base}/{filename}.json', 'w') as f:
#         if type(result) == list:
#             f.write(json.dumps(result, indent=ind))
#         else:
#             f.write(json.dumps(result.json(), indent=ind))