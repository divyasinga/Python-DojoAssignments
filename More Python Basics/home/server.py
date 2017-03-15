from flask import Flask, redirect, flash, request, render_template, session

app = Flask(__name__)
app.secret_key = "THIS IS MY SECRET KEY DO NOT TELL ANYONE"

@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/indy')
def indy():
    if 'trip_history' in session:
        history = session['trip_history']
        history.insert(0, "Visited Pawnee")
        session['trip_history'] = history
    return render_template('/indiana.html')

@app.route('/cali')
def cali():
    if 'trip_history' in session:
        history = session['trip_history']
        history.insert(0, "Visited California")
        session['trip_history'] = history
    return render_template('/california.html')

@app.route('/ny')
def ny():
    if 'trip_history' in session:
        history = session['trip_history']
        history.insert(0, "Visited New York")
        session['trip_history'] = history
    return render_template('/newyork.html')   

@app.route('/login')
def login():
    return render_template('/login.html')  

@app.route('/auth', methods=['POST'])
def auth():
    form_email = request.form['html_email']
    form_pw = request.form['html_pw']
    if form_email == 'user@gmail.com' and form_pw == 'asdfasdf':
        session['username'] = "SomeUser42"
        session['email'] = form_email
        session['trip_history'] = []
        return render_template('/index.html', template_email = form_email, template_pw = form_pw)
    else:
        return redirect('/login')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

app.run(debug=True)