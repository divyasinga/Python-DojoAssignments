from django.shortcuts import render, redirect, HttpResponse
from .models import Email
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "validator/index.html")

def validate(request):
    if request.method == 'POST':
        if Email.emailManager.validate(request.POST['email']):
            Email.emailManager.create(email=request.POST['email'])
            context = {
                'emails': Email.emailManager.all(),
            }
            request.session['email'] = request.POST['email']
            return render(request, 'validator/emails.html', context)
        else:
            messages.error(request, 'Invalid email!')
            return redirect('/')