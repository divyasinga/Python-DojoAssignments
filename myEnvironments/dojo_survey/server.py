from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/result', methods=['POST'])
def create_user():
  name = request.form['name']
  language = request.form['language']
  location = request.form['dojo']
  comments = request.form['comment']

  return render_template('result.html', name=name, location=location, language=language, comments=comments)

app.run(debug=True)