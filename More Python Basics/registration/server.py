# import Flask
from flask import Flask, render_template, redirect, request, session, flash
# the "re" module will let us perform some regular expression operations
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX =  re.compile(r'^[a-zA-Z]+$')
PW_REGEX = re.compile(r'^(?=.{8,32}$)(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).*')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")
  
@app.route('/process', methods=['POST'])
def submit():
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!", "emailerror")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!", "emailerror")
    elif not PW_REGEX.match(request.form['password']):
        flash("Password needs at least 1 uppercase and 1 number", "pwformat")
    elif len(request.form['first_name']) < 1 or len(request.form['last_name']) < 1:
        flash("Name cannot be blank!", "nameerror")
    elif len(request.form['password']) < 1 or len(request.form['confirm']) < 1:
        flash("Password and confirm required", "pwerror")
    elif len(request.form['password']) < 8:
        flash("Password must be more than 8 characters", "shortpw")
    elif request.form['password'] != request.form['confirm']:
        flash("Password and confirm must match", "pwmatch")
    elif not NAME_REGEX.match(request.form['first_name']) or not NAME_REGEX.match(request.form['last_name']):
        flash("Name cannot contain numbers", "nameformat")
    else:
        flash("Success!")
    return redirect('/')
app.run(debug=True)
