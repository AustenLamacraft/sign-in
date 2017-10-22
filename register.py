import random

from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL

from werkzeug import generate_password_hash, check_password_hash

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'austen'
app.config['MYSQL_DATABASE_PASSWORD'] = 'alam5sql'
app.config['MYSQL_DATABASE_DB'] = 'tqm_register'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'alam63sql'
# app.config['MYSQL_DATABASE_DB'] = 'tqm2017'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)


@app.route('/', methods=['POST','GET'])
def main():
    try:
        conn = mysql.connect()

        with conn.cursor() as cursor:
            # Read a single record
            sql = "SELECT `user_name`, `user_username` FROM `tbl_user`"
            # sql = "SELECT `user_name` FROM `wp_useronline`  WHERE `timestamp` + 5400 > NOW()"
            # cursor.execute(sql, ('webmaster@python.org',))
            cursor.execute(sql)
            online_users = cursor.fetchall()
            app.logger.info(online_users)

    finally:
        conn.close()

    # return jsonify(online_users)

    if request.method == 'POST':
        jumbo = random.choice(online_users)[0]
    else:
        jumbo = ""

    return render_template('users.html', users=online_users, jumbo=jumbo)


if __name__ == "__main__":
    app.run()
