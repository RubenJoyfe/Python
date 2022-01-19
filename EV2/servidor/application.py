from flask import Flask

appplication = Flask(__name__)

@appplication.route("/")
def hello_world():
    return "<p>Hello, World!</p>"