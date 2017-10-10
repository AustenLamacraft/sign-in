# from flask import Flask
# from flask_raven import raven_auth
#
# signin = Flask(__name__)
#
# signin.config.update(
#     SECRET_KEY='super-secret-key'
# )
#
#
# @signin.route('/')
# @raven_auth()
# def home():
#     return "Logged in"
#
# if __name__ == '__main__':
#     signin.run(debug=True)

# from flask_raven import raven_auth

from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
