from distutils.dep_util import newer
from flask import Flask, request, jsonify, abort
from datetime import datetime, timedelta
from functools import wraps
from itsdangerous import exc
import requests, json, os, jwt

application = Flask(__name__)
path_base = os.path.dirname(os.path.abspath(__file__))

def token_required(f):
    @wraps(f)
    def decorated(*args, **kargs):
        try:
            token = request.headers['Authorization'].split()[1]
            user_data = jwt.decode(token, 'ContraseñaSuperSecretaQuenodeberíaSaberNADIE:=)', algorithms=['HS256'])
            return f(user_data['id'], *args, **kargs)
        except Exception as e:
            abort(401)
        pass
    return decorated

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
                        'type': 1,
                        'exp': datetime.utcnow() + timedelta(minutes=1)
                    }
                    , 'ContraseñaSuperSecretaQuenodeberíaSaberNADIE:=)', algorithm='HS256')
                return jsonify({
                    "username": usr['username'],
                    "token": token
                }), 200
    return '', 401

@application.route("/users", methods=['POST'])
@token_required
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
                "email": data['pass'],
                "address": {
                    "street": "",
                    "suite": "",
                    "city": "",
                    "zipcode": "",
                "geo": {
                    "lat": "",
                    "lng": ""
                }
                },
                "phone": "",
                "website": "",
                "company": {
                    "name": "",
                    "catchPhrase": "",
                    "bs": ""
                }
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