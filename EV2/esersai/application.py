from distutils.dep_util import newer
from enum import IntEnum
from flask import Flask, request, jsonify, abort
from socketio import *
from datetime import datetime, timedelta
from functools import wraps
from itsdangerous import exc
import requests, json, os, jwt

application = Flask(__name__)
path_base = os.path.dirname(os.path.abspath(__file__))
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
    with open(f'{path_base}/users.json', 'r') as f:
        users=json.loads(f.read())
    for usr in users:
        if usr['username'] == request.form['user']:
            if usr['email'] == request.form['pass']:
                token = jwt.encode(
                    {
                        "id": usr['id'],
                        'type': 5,
                        'exp': datetime.utcnow() + timedelta(hours=24)
                    }
                    , JSON_KEY, algorithm='HS256')
                return jsonify({
                    "username": usr['username'],
                    "token": token
                }), 200
    return '', 401

@application.route("/users", methods=['POST'])
@check_auth(UserType.ADMIN)
def create_user(user_id):
    # if'Authorization' not in request.headers:
    #     return 'Sin autenticación', 403
    # token = request.headers['Authorization'].split()[1]
    # try:
    #     user_data = jwt.decode(token, 'ContraseñaSuperSecretaQuenodeberíaSaberNADIE:=)', algorithms=['HS256'])
    # except Exception as e:
    #     return str(e), 401

    # if user_data['type'] != 1:
    #     return 'No tienes permisos para crear usuarios', 403

    data = request.get_json() # Obtener el json de la peticion
    # Leo el archivo de usuarios y lo guardo
    with open(f'{path_base}/users.json', 'r') as f:
        users=json.loads(f.read())
    # BUSCAR NUEVA ID
    newId = max([usr['id'] for usr in users]) + 1
    # ESTRUCTURA USUARIO CON SUS DATOS
    # new_user = dict.fromkeys(list(users[0].keys()))
    # new_user['id'] = newId
    # new_user['name'] = data['user']
    # new_user['username'] = data['user']
    # new_user['email'] = data['pass']
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