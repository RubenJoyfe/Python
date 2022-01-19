from flask import *
from markupsafe import escape

application = Flask(__name__)

@application.route("/")
def hello_world():
    return "<p>Hola, JijiJA!</p>"

@application.route("/<name>")
def hello(name):
    return f"<h1>Hello, {escape(name)}!</h1>"

@application.route("/login", methods = ['POST'])
def login():
    if request.form['pass'] != '1234':
        abort(401)
        return "Hacker!!!"
    # return "Hola " + request.form['user']
    return jsonify({'user': request.form['user']}), 200

@application.route("/user/<int:user>", methods = ['GET'])
def get_user(user):
    return f"<h1>Hola, {user}</h1>"

@application.route("/user/<int:user>", methods = ['POST'])
def new_user(user):
    return f"<h1>Hola desde POST, {user}</h1>"

if __name__ == "__main__":
    application.run(debug=True)