from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import User
import bcrypt
import re

def index(request):
    return render(request, 'loggy/index.html')

def register(request):
    if request.method == 'POST':
        if User.objects.validate(request.POST['email']) and User.objects.validpw(request.POST['regpw']) and (request.POST['regpw'] == request.POST['regconfirm']):
            hashed = bcrypt.hashpw(request.POST['regpw'].encode(), bcrypt.gensalt())
            User.objects.create(email=request.POST['email'], password=hashed, first_name=request.POST['first_name'], last_name=request.POST['last_name'])
            context = {
                'emails': User.objects.all(),
            }
            request.session['email'] = request.POST['email']
            return render(request, 'loggy/emails.html', context)
        elif User.objects.validate(request.POST['email']) == False:
            messages.error(request, 'Invalid email!')
            return redirect(reverse('users:loggy_index'))
        elif User.objects.validpw(request.POST['regpw']) == False:
            messages.error(request, 'Invalid password!')
            return redirect(reverse('users:loggy_index'))
        elif (request.POST['regpw'] != request.POST['regconfirm']):
            messages.error(request, 'Passwords do not match!')
            return redirect(reverse('users:loggy_index'))
        elif User.objects.get(email=request.POST['email']) == True:
            messages.error(request, 'User already exists')
            return redirect(reverse('users:loggy_index'))
        else:
            return redirect(reverse('users:loggy_index'))

def login(request):
    if request.method == 'POST':
        loginemail = request.POST['loginemail']
        loginpw = request.POST['loginpw'].encode()
        user = User.objects.get(email=loginemail)
        if bcrypt.hashpw(loginpw, user.password.encode()) == user.password.encode():
            context = {
                'emails': User.objects.all(),
            }
            request.session['email'] = loginemail
            return render(request, 'loggy/emails.html', context)
        else:
            return redirect(reverse('users:loggy_index'))