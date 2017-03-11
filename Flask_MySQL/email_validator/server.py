from flask import Flask, session, redirect, render_template, request, flash
from mysqlconnection import MySQLConnector

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
mysql = MySQLConnector(app,'emailsdb')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validate', methods=['POST'])
def valid():
    if not EMAIL_REGEX.match(request.form['emailinput']):
        flash('Email format invalid')
        return redirect('/')
    else:
        session['newemail'] = request.form['emailinput']
        query = "INSERT INTO emaillist (user_email, created_at) VALUES (:user_email, NOW())"
        data = {'user_email': request.form['emailinput']}
        mysql.query_db(query,data)
        return redirect('/success')

@app.route('/success')
def success():
    query = "SELECT * FROM emaillist"
    emails = mysql.query_db(query)
    return render_template('success.html', all_emails=emails)

@app.route('/remove_email/<email_id>', methods=['POST'])
def delete(email_id):
    query = 'DELETE FROM emaillist WHERE id = :id'
    data = {'id': email_id}
    mysql.query_db(query, data)
    return redirect('/success')

app.run(debug=True)