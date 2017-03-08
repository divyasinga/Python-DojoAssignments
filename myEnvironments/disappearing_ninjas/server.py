from flask import Flask, flash, redirect, render_template, session, request

app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

@app.route('/', methods=['GET'])
def index():
  return render_template("index.html")

@app.route('/ninja', methods=['GET'])
def ninja():
  return render_template("ninja.html")

@app.route('/ninja/<color>', methods=['GET'])
def ninjacolor(color):
    if color == "blue":
        return render_template("blueninja.html")
    if color == "red":
        return render_template("redninja.html")
    if color == "purple":
        return render_template("purpleninja.html")
    if color == "orange":
        return render_template("orangeninja.html")
    else:
        return render_template("april.html")

app.run(debug=True)