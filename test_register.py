from flask import Flask, render_template, json, request, redirect, jsonify
from flaskext.mysql import MySQL

from werkzeug import generate_password_hash, check_password_hash

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'austen'
app.config['MYSQL_DATABASE_PASSWORD'] = 'alam5sql'
app.config['MYSQL_DATABASE_DB'] = 'tqm_register'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/doom')
def online_users():
    try:

        conn = mysql.connect()

        with conn.cursor() as cursor:
            # Read a single record
            sql = "SELECT `user_name`, `user_username` FROM `tbl_user`" # WHERE `email`=%s"
            # cursor.execute(sql, ('webmaster@python.org',))
            cursor.execute(sql)
            online_users = cursor.fetchall()
            app.logger.info(online_users)

    finally:
        conn.close()

    # return jsonify(online_users)
    return render_template('users.html', users=online_users)



@app.route('/signUp',methods=['POST','GET'])
def signUp():
    if request.method == 'POST':
        try:
            _name = request.form['inputName']
            _email = request.form['inputEmail']
            _password = request.form['inputPassword']

            # validate the received values

            if _name and _email and _password:

                # All Good, let's call MySQL
                _hashed_password = generate_password_hash(_password)


                conn = mysql.connect()

                with conn.cursor() as cursor:

                    check = cursor.callproc('sp_createUser',(_name,_email,_hashed_password))
                    data = cursor.fetchall()


                if len(data) is 0:
                    conn.commit()
                    conn.close()
                    return json.dumps({'message':'User created successfully !'})

                else:
                    app.logger.info(data)
                    conn.close()

                    return json.dumps({'error':str(data[0])})


            else:
                return json.dumps({'html':'<span>Enter the required fields</span>'})



        except Exception as e:
                return json.dumps({'error':str(e)})

    else:
        return render_template('signUp.html')

@app.route('/signUp2',methods=['POST','GET'])
def signUp2():
    if request.method == 'POST':
        app.logger.info("here!")
        # return json.dumps("Hi!")
        # return render_template('index.html')
        return jsonify(dict(redirect='/'))
        # return redirect('/puttest/')

    else:
        return render_template('signUp.html')

@app.route('/loggedIn')
def loggedIn():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
