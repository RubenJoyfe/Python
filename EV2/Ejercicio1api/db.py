from turtle import update
from unittest import result
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB+Compass&ssl=false')

db = client.python2b

# filter = {'user': 'admin'}
# projection = {}
# user = db.test.find_one(filter, projection)
# print(user)


# filter = {}
# projection = {'user': 1, '_id': 0}
# users = db.test.find(filter, projection)
# for u in users:
#     print(u)

# # Creamos un usuario
# new_user = {
#     'nick': 'admin1',
#     'pass': '123456'
# }
# result = db.test.insert_one(new_user)
# print(result.inserted_id)
# # Borramos el usuario que acabamos de insertar
# filter = {'nick': 'admin1'}
# result = db.test.delete_one(filter)
# print(result.deleted_count)

# # Actualizamos el usuario
# filter = {'nick': 'admin1'}
# update = {'$set': {'nick': 'admin', 'login': True}}
# result = db.test.update_one(filter, update)

#
from distutils.dep_util import newer
from enum import IntEnum
from flask import Flask, request, jsonify, abort
from datetime import datetime, timedelta
from functools import wraps
from itsdangerous import exc
import requests, json, os, jwt

application = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB+Compass&ssl=false')
db = client.python2b
JSON_KEY = 'ContraseñaSuperSecretaQuenodeberíaSaberNADIE:=)'

class UserType(IntEnum):
    SUPERADMIN = 1
    ADMIN = 5
    GESTOR = 10
    USUARIO = 1000

def check_auth(role):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kargs):
            try:
                token = request.headers['Authorization'].split()[1]
                user_data = jwt.decode(token, 'ContraseñaSuperSecretaQuenodeberíaSaberNADIE:=)', algorithms=['HS256'])
                if user_data['type'] > role:
                    abort(401)
                return f(user_data['id'], *args, **kargs)
            except Exception as e:
                abort(401)
            pass
        return wrapper
    return decorator

@application.route("/")
def hello_world():
    return "<h1>Hola, World!</h1>"

@application.route("/login", methods=['POST'])
def login():
    filter = {'user': request.form['user'], 'pass': request.form['pass']}
    projection = {'type': 1}
    user = db.test.find_one(filter, projection)
    
    if user:
        token = jwt.encode(
            {
                "id": str(user['_id']),
                'type': user['type'],
                'exp': datetime.utcnow() + timedelta(hours=24)
            }
            , JSON_KEY, algorithm='HS256')
        return jsonify({
            "id": str(user['_id']),
            "token": token
        }), 200 
    return '', 401

@application.route("/users", methods=['POST'])
@check_auth(UserType.ADMIN)
def create_user(user_id):
    data = request.get_json() # Obtener el json de la peticion
    # Leo el archivo de usuarios y lo guardo
    with open(f'{path_base}/users.json', 'r') as f:
        users=json.loads(f.read())
    # BUSCAR NUEVA ID
    newId = max([usr['id'] for usr in users]) + 1
    # ESTRUCTURA USUARIO CON SUS DATOS
    new_user = {
                "id": newId,
                "name": data['user'],
                "username": data['user'],
                "email": data['pass']
                }
    # Agrego el usuario introducido y guardo en el fichero los usuarios
    users.append(new_user)
    with open(f'{path_base}/users.json', 'w') as f:
        f.write(json.dumps(users, indent=4))
    return 'Usuario creado', 201

@application.route("/user/<int:user_id>", methods=['GET'])
def get_user(user_id):
    # Leo el archivo de usuarios y lo guardo
    with open(f'{path_base}/users.json', 'r') as f:
        users=json.loads(f.read())
    for user in users:
        if user['id'] == user_id:
            return jsonify(user), 200


@application.route("/user/<string:user>", methods=['POST'])
def new_user(user):
    return f"Hola desde POST, {user}"

if __name__ == '__main__':
    application.run(debug=True)