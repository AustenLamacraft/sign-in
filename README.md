## Notes

- `flaskext` had no `__init__.py` after install on MWS. I had to add one.

- `.wsgi` expected to contain a `from --- import app as application` 

## A guide

[Creating a Web App From Scratch Using Python Flask and MySQL](https://code.tutsplus.com/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972)

Some problems in this guide

- Import `Flask-MySQL` with `import flaskext.mysql`

- Stored procedure in database limited entries to 20 characters! Emails can be longer, and hashed passwords much longer. I increased to 45 characters for the former; 120 characters for latter.

- `conn.close()` and `cursor.close()` could happen before declaration. I wrapped in `with` statements instead. But then we have [this issue](https://github.com/PyMySQL/PyMySQL/issues/248), that the `__enter__()` method for connections returns a cursor, so I switched this back.

## MWS setup

On MWS I use the following `.htaccess`

```
AddHandler wsgi-script .wsgi

Options FollowSymlinks ExecCGI MultiViews Indexes
MultiviewsMatch Handlers

RewriteEngine on
RewriteBase /
RewriteRule ^(signin(/)?)$  /signin/signin.wsgi  [L,QSA]
```

Answered questions so far: ygp2, hmb59, ap948


## MySQL basics

`mysql -u root -p`

Enter root password

`GRANT ALL PRIVILEGES ON *.* TO 'user'@'localhost' IDENTIFIED BY 'mysuperpwd';`

`UPDATE mysql.user SET Password=PASSWORD('your_new_password')
       WHERE User='root';
ERROR 1820 (HY000): You must reset your password using ALTER USER statement before executing this statement.
mysql> SET PASSWORD = PASSWORD('your_new_password');`

`\q` to quit

`mysql -u al200 -p`

Enter new user password

`CREATE DATABASE tqm_register;`

## Logging user logins

[LAST LOGIN OF MYSQL DATABASE USERS](http://www.fromdual.com/last-login-off-mysql-database-users)
