from flask import Flask, request, jsonify, abort
import requests, json, os

application = Flask(__name__)
path_base = os.path.dirname(os.path.abspath(__file__))

@application.route("/")
def hello_world():
    return "<h1>Hola, World!</h1>"

@application.route("/login", methods=['POST'])
def login():
    users = []
    with open(f'{path_base}/users.json', 'r') as f:
        users=json.loads(f.read())
    for usr in users:
        if usr['username'] == request.form['user']:
            if usr['website'] == request.form['pass']:
                return jsonify({'user': usr['username']}), 200
    # abort(401)
    return 'Hacker!!!', 401
    return jsonify({'usuario': request.form['user']}), 200

@application.route("/user/<string:user>", methods=['GET'])
def get_user(user):
    return f"Hola, {user}"

@application.route("/user/<string:user>", methods=['POST'])
def new_user(user):
    return f"Hola desde POST, {user}"

if __name__ == '__main__':
    application.run(debug=True)