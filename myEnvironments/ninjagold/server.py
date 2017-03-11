from flask import Flask, render_template, request, redirect, session
import random
import datetime

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    elif 'activity' not in session:
        session['activity'] = "Time to make some money."
    return render_template("index.html")

@app.route('/process_gold', methods=["POST"])
def process():
    if request.form['acquisition'] == 'farm':
        session['farmgold'] = random.randrange(10,20)
        session['gold'] += session['farmgold']
        session['activity'] = "You got " + str(session['farmgold']) + " gold while farming. " + datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S') + "\n" + session['activity']
        return redirect('/')
    elif request.form['acquisition'] == 'cave':
        session['cavegold'] = random.randrange(5,10)
        session['gold'] += session['cavegold']
        session['activity'] = "You got " + str(session['cavegold']) + " gold while farming. " + datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S') + "\n" + session['activity']
        return redirect('/')
    elif request.form['acquisition'] == 'house':
        session['housegold'] = random.randrange(2,5)
        session['gold'] += session['housegold']
        session['activity'] = "You got " + str(session['housegold']) + " gold while farming. " + datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')+ "\n" + session['activity']
        return redirect('/')
    elif request.form['acquisition'] == 'dabo':
        session['casinogold'] = random.randrange(-50,51)
        session['gold'] += session['casinogold']
        if int(session['casinogold']) > 0:
            session['activity'] = "You won " + str(session['casinogold']) + " gold at the Dabo Table! " + datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S') + "\n" + session['activity']
        else:
            session['activity'] = "Yikes. You lost " + str(session['casinogold']*-1) + " gold at the Dabo Table. " + datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S') + "\n" + session['activity']
        return redirect('/')
    elif request.form['acquisition'] == 'bankrupt':
        session.pop('activity')
        session.pop('gold')
        session['gold'] = 0
        session['activity'] = "Time to make some money."
        return redirect('/')

app.run(debug=True)