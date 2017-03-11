from flask import Flask, session, request, redirect, render_template, flash
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
app.secret_key = "MemberFriendster"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mysql = MySQLConnector(app,'fullfriends')

@app.route('/')
def index():
    query = "SELECT * FROM friends"
    allfriends = mysql.query_db(query)
    return render_template('/index.html', allfriends=allfriends)

@app.route('/addfriend', methods=['POST'])
def addfriend():
    query = 'INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())'
    data = {
    'first_name': request.form['first_name'],
    'last_name': request.form['last_name'],
    'email': request.form['email']
    }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/deletefriend/<id>', methods=['POST'])
def deletefriend(id):
    query = 'DELETE FROM friends WHERE id = :id'
    data = {
        'id': id
    }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/editfriend/<id>')
def edit(id):
    query = "SELECT * FROM friends WHERE id = :id"
    data = {
        "id": id
    }
    allfriends = mysql.query_db(query, data)
    session['data'] = id
    return render_template('edit-friends.html', allfriends=allfriends)


@app.route('/submitedit', methods=['POST'])
def submitdata():

    query = 'UPDATE friends SET first_name = :first_name, last_name = :last_name, email = :email, updated_at = NOW() WHERE id = :id'
    
    data = {
    'first_name': request.form['first_name'],
    'last_name': request.form['last_name'],
    'email': request.form['email'],
    'id': session['data']
    }

    mysql.query_db(query, data)
    session.clear()
    return redirect('/')

app.run(debug=True)