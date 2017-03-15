from django.shortcuts import render, HttpResponse, redirect
import random

# Create your views here.
def index(request):
    if 'attempt' not in request.session:
        request.session['attempt'] = 1
    return render(request, 'randomWord/index.html')

def generate(request):
    x = ['longing', 'rusted', 'daybreak', 'furnace', 'nine', 'benign', 'homecoming', 'one', 'freightcar']
    request.session['attempt'] += 1
    request.session['generatedWord'] = random.choice(x)
    return redirect('/')