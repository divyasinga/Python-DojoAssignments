from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
@app.route('/')
def index():
  return render_template("index.html")

@app.route('/result', methods=['POST'])
def create_user():
  if len(request.form['name']) < 1:
    flash("Name field is required", "namefield")
    return redirect('/')
  elif len(request.form['comment']) > 120:
    flash("Comment must be under 120 characters", "commentfield")
    return redirect('/')
  else:
    name = request.form['name']
    language = request.form['language']
    location = request.form['dojo']
    comments = request.form['comment']
    return render_template('result.html', name=name, location=location, language=language, comments=comments)

app.run(debug=True)