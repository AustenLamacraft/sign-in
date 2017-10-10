from flask import Flask
from flask_raven import raven_auth

signin = Flask(__name__)

signin.config.update(
    SECRET_KEY='super-secret-key'
)


@signin.route('/')
@raven_auth()
def home():
    return "Logged in"

if __name__ == '__main__':
    signin.run(debug=True)

# from signin.flask_raven import raven_auth
#
# signin = Flask(__name__)
#
# @signin.route('/')
# def hello():
#     return "Hello World!"
