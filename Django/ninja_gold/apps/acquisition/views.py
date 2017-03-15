from django.shortcuts import render, redirect, HttpResponse
import random
import datetime

# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['activity'] = "Time to make some money."
    return render(request, 'acquisition/index.html')

def acquisition(request, id):
    if request.method == "POST":
        if id == 'farm':
            request.session['farmgold'] = random.randrange(10,20)
            request.session['gold'] = request.session['gold'] + request.session['farmgold']
            request.session['activity'] = "You got " + str(request.session['farmgold']) + " gold while farming. " + datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S') + "\n" + request.session['activity']
        elif id == 'cave':
            request.session['cavegold'] = random.randrange(5,10)
            request.session['gold'] = request.session['gold'] + request.session['cavegold']
            request.session['activity'] = "You found " + str(request.session['cavegold']) + " gold while in a cave. " + datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S') + "\n" + request.session['activity']
        elif id == 'house':
            request.session['housegold'] = random.randrange(2,5)
            request.session['gold'] = request.session['gold'] + request.session['housegold']
            request.session['activity'] = "I don't know whose house your'e in, but you just got " + str(request.session['housegold']) + " gold from their house! " + datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')+ "\n" + request.session['activity']
        elif id == 'dabo':
            request.session['dabogold'] = random.randrange(-50,51)
            request.session['gold'] = request.session['gold'] + request.session['dabogold']
            if request.session['dabogold'] > 0:
                request.session['activity'] = "You won " + str(request.session['dabogold']) + " gold at the Dabo Table! " + datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S') + "\n" + request.session['activity']
            elif request.session['dabogold'] < 0:
                request.session['activity'] = "Yikes. You lost " + str(-request.session['dabogold']) + " gold at the Dabo Table... " + datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S') + "\n" + request.session['activity']
            else:
                 request.session['activity'] = "Nothing gained, nothing lost." + request.session['activity']
        elif id == 'bankrupt':
            request.session['gold'] = 0
            request.session['activity'] = 'Time to make some money.'
        return redirect('/')
    else:
        return redirect('/')