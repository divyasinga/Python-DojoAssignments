from flask import Flask, session, request, render_template, redirect, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
mysql = MySQLConnector(app, 'walldb')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app.secret_key = "WatchersOnTheWall"
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['loginemail']
    pw = request.form['loginpw']
    user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    query_data = { 'email': email }
    user = mysql.query_db(user_query, query_data)
    if user[0]['password'] == pw:
        session['user'] = user[0]['first_name']
        session['id'] = user[0]['id']
        print session['id']
        return redirect('/wall')
    else:
        flash('Invalid username or password', 'loginerror')
        return redirect('/')

@app.route('/register', methods=['POST'])
def register():
    firstname = request.form['htmlfirst_name']
    lastname = request.form['htmllast_name']
    email = request.form['htmlemail']
    pw = request.form['htmlpw']
    confirm = request.form['htmlconfirm']

    if len(firstname) < 2 or len(lastname) < 2:
        flash('Name must be at least 2 characters', 'nameerror')
        return redirect('/')
    elif not EMAIL_REGEX.match(email):
        flash('Email format is invalid', 'emailerror')
        return redirect('/')
    elif pw != confirm:
        flash('Passwords do not match', 'pwerror')
        return redirect('/')
    else:
        # write new user into db
        query = 'INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())'
        data = {
            'first_name': firstname,
            'last_name': lastname,
            'email': email,
            'password': pw
        }
        mysql.query_db(query, data)
        session['user'] = firstname
        
        # new query to pull id of new user from db
        user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
        query_data = { 'email': email }
        user = mysql.query_db(user_query, query_data)
        session['id'] = user[0]['id']
        return redirect('/wall')

@app.route('/wall')
def wall():
    if 'user' in session:
        query = "SELECT messages.message, messages.created_at, users.first_name, users.last_name, messages.id, messages.user_id FROM messages JOIN users on (users.id = messages.user_id) ORDER by created_at DESC"
        messages = mysql.query_db(query)
        query2 = "SELECT comments.comment_text, comments.created_at, users.first_name, users.last_name, comments.message_id, messages.id FROM comments JOIN messages on (comments.message_id = messages.id) JOIN users on (comments.user_id = users.id) ORDER by created_at DESC"
        comments = mysql.query_db(query2)
        deletequery = "SELECT users.id, messages.user_id FROM messages JOIN users on (users.id = messages.user_id)"
        deletes = mysql.query_db(deletequery)
        return render_template('wall.html', messages=messages, comments=comments, deletes=deletes, user=session['id'])
    else:
        return redirect('/')

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/')

@app.route('/post', methods=['POST'])
def post():
    posttext = request.form['posttext']
    userid = session['id']
    print posttext
    if len(posttext) > 0:
        query = 'INSERT INTO messages (message, user_id, created_at, updated_at) VALUES (:message, :user_id, NOW(), NOW())'
        data = {
            'message': posttext,
            'user_id': userid
        }
        mysql.query_db(query, data)
        return redirect('/wall')
    else:
        flash('You have to type something to post.', 'posterror')
        return redirect('/wall')

@app.route('/comment/<postid>', methods=['POST'])
def comment(postid):
    commenttext = request.form['commenttext']
    userid = session['id']
    if len(commenttext) > 0:
        query = 'INSERT INTO comments (comment_text, user_id, message_id, created_at, updated_at) VALUES (:message, :user_id, :message_id, NOW(), NOW())'
        data = {
            'message': commenttext,
            'user_id': userid,
            'message_id': postid
        }
        mysql.query_db(query, data)
        return redirect('/wall')
    else:
        flash('You have to type something to comment.', 'commenterror')
        return redirect('/wall')

@app.route('/delete/<postid>', methods=['POST'])
def delete(postid):
    # if statement to confirm user is in session
    deletepostcomments = 'DELETE from comments WHERE message_id = :id'
    data = {
        'id': postid
    }
    mysql.query_db(deletepostcomments, data)

    query = 'DELETE from messages WHERE id = :id'
    data = {
        'id': postid
    }
    mysql.query_db(query, data)
    return redirect('/wall')

app.run(debug=True)