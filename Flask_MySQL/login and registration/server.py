from flask import Flask, session, request, render_template, redirect, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re

app = Flask(__name__)
app.secret_key = "BcryptKeeper"
bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mysql = MySQLConnector(app,'logindb')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    print request.form['htmlfirstname']
    if not EMAIL_REGEX.match(request.form['htmlemail']):
        flash('Email format invalid', 'emailerror')
        return redirect('/')
    elif request.form['htmlpw'] != request.form['htmlconfirm']:
        flash('Passwords must match', 'pwerror')
        return redirect('/')
    elif len(request.form['htmlfirstname']) < 2 or len(request.form['htmllastname']) < 2:
        flash('First and Last name must be at least two characters each.', 'nameerror')
        return redirect('/')
    else:
        session['user'] = request.form['htmlemail']

        password = request.form['htmlpw']
        pw_hash = bcrypt.generate_password_hash(request.form['htmlpw'])

        query = 'INSERT INTO users (first_name, last_name, email, password) VALUES (:first_name, :last_name, :email, :password)'
        data = {
            'first_name': request.form['htmlfirstname'],
            'last_name': request.form['htmllastname'],
            'email': request.form['htmlemail'],
            'password': pw_hash
        }

        print query
        print data
        print '===================================================='
        mysql.query_db(query,data)
        return redirect('/success')

@app.route('/success')
def success():
    if 'user' in session:
        return render_template('success.html')
    else:
        return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['loginemail']
    password = request.form['loginpw']
    user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    query_data = { 'email': email }
    user = mysql.query_db(user_query, query_data)
    if bcrypt.check_password_hash(user[0]['password'], password):
        session['user'] = request.form['loginemail']
        return redirect('/success')
    else:
        flash('Incorrect usrname or password', 'loginfail')
        return redirect('/')

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/')

app.run(debug=True)