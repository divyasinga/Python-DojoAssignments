from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    return render(request, 'surveyForm/index.html')

def submit(request):
    if request.method == 'POST':
        request.session['counter'] += 1
        request.session['sessionname'] = request.POST['yourname']
        request.session['sessionloc'] = request.POST['location']
        request.session['sessionlang'] = request.POST['language']
        request.session['sessioncomm'] = request.POST['comments']
        print '==================================='
        print request.session['counter']
        return redirect('/results')
    else:
        print '**********************************'
        print request.session['counter']
        return redirect('/')

def results(request):
    return render(request, 'surveyForm/results.html')