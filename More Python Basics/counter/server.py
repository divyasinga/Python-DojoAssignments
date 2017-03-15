from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

def sumSessionCounter():
  try:
    session['counter'] += 1
  except KeyError:
    session['counter'] = 1

@app.route('/')
def index():
  sumSessionCounter()
  return render_template("index.html")

@app.route('/double', methods=["POST"])
def doublesession():
    sumSessionCounter()
    return redirect('/')

@app.route('/clear', methods=["POST"])
def clearsession():
    session.clear()
    return redirect('/')

app.run(debug=True)