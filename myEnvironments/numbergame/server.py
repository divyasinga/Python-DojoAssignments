from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    session['randomnum'] = random.randrange(0, 101)
    print session['randomnum']
    return render_template("index.html")

@app.route('/guess', methods=["POST"])
def guess():
    print session['randomnum']
    session['guess'] = int(request.form['guessdata'])
    print session['guess']
    if session['guess'] > session['randomnum']:
        return redirect('/toohigh')
    elif session['guess'] < session['randomnum']:
        return redirect('/toolow')
    else:
        return redirect('/justright')

@app.route('/toohigh')
def toohigh():
    return render_template("toohigh.html")

@app.route('/toolow')
def toolow():
    return render_template("toolow.html")

@app.route('/justright')
def winner():
    return render_template("justright.html")

@app.route('/replay', methods=['POST'])
def replay():
    session.pop('randomnum')
    return redirect("/")

app.run(debug=True)