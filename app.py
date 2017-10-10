from flask import Flask
signin = Flask(__name__)

@signin.route('/')
def hello():
    return "Hello World!"
