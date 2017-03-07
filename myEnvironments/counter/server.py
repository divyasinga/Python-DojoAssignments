from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

def sumSessionCounter():
  try:
    session['counter'] += 1
  except KeyError:
    session['counter'] = 1

def sumSessionCounter2():
  try:
    session['counter'] += 2
  except KeyError:
    session['counter'] = 2

@app.route('/')
def index():
  sumSessionCounter()
  return render_template("index.html", counter='counter')
  print counter

@app.route('/double', methods=["POST"])
def doublesession():
    sumSessionCounter2()
    return render_template("index.html", counter='counter')

@app.route('/clear', methods=["POST"])
def clearsession():
    session.clear()
    return redirect('/')

app.run(debug=True)