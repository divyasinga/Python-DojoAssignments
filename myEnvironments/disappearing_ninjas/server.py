from flask import Flask, flash, redirect, render_template, session, request

app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

@app.route('/', methods=['GET'])
def index():
    session['turtle'] = "tmnt.png"
    return render_template("index.html")

@app.route('/ninja', methods=['GET'])
def ninja():
    return render_template("ninja.html")

@app.route('/ninja/<color>', methods=['GET'])
def ninjacolor(color):
    if color == "blue":
        session['turtle'] = "leonardo.jpg"
        return redirect("/ninja")
    if color == "red":
        session['turtle'] = "raphael.jpg"
        return redirect("/ninja")
    if color == "purple":
        session['turtle'] = "donatello.jpg"
        return redirect("/ninja")
    if color == "orange":
        session['turtle'] = "michelangelo.jpg"
        return redirect("/ninja")
    else:
        session['turtle'] = "notapril.jpg"
        return redirect("/ninja")

app.run(debug=True)