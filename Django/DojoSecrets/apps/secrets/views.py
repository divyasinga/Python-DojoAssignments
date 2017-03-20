from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.db.models import Count
from django.core.urlresolvers import reverse
from .models import *
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'secrets/index.html')

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['confirm']
        if User.objects.validate(email) and User.objects.validpw(password) and password == confirm:
            try:
                User.objects.get(email=email)
                messages.error(request, "User already exists.")
                return redirect(reverse('secrets:secrets_index'))
            except (User.DoesNotExist):
                hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
                User.objects.create(email=email, password=hashed, first_name=first_name, last_name=last_name)
                request.session['user'] = first_name
                user = User.objects.get(email=email)
                request.session['id'] = user.id
                return redirect(reverse('secrets:secrets_recent'))
        elif User.objects.validate(email) == False:
            messages.error(request, "Invalid email!")
            return redirect(reverse('secrets:secrets_index'))
        elif User.objects.validpw(password) == False:
            messages.error(request, "Invalid password. Must contain one uppercase, one lowercase, and one number.")
            return redirect(reverse('secrets:secrets_index'))
        elif password != confirm:
            messages.error(request, "Passwords do not match.")
            return redirect(reverse('secrets:secrets_index'))

def login(request):
    if request.method == 'POST':
        loginemail = request.POST['user_email']
        loginpw = request.POST['user_pw'].encode()
        user = User.objects.get(email=loginemail)
        if bcrypt.hashpw(loginpw, user.password.encode()) == user.password.encode():
            request.session['user'] = user.first_name
            request.session['id'] = user.id
            return redirect(reverse('secrets:secrets_recent'))
        else:
            return redirect('/')

def recent(request):
    likes = {}
    for like in Like.objects.filter(user_id=request.session['id']):
        likes[like.secret_id] = True

    context = {
        'secrets': Secret.objects.all().order_by('-created_at'),
        'likes': likes,
    }

    return render(request, 'secrets/recent.html', context)

def submit(request):
    if request.method == 'POST':
        text = request.POST['submitsecret']
        Secret.objects.create(secret_text=text)
        return redirect(reverse('secrets:secrets_recent'))

def popular(request):
    context = {
        'secrets': Secret.objects.all().annotate(like_count=Count('likes')).order_by('-like_count'),
    }
    return render(request, 'secrets/popular.html', context)

def like(request, id):
    secret_id = Secret.objects.get(id=id)
    user_id = User.objects.get(id=request.session['id'])
    try:
        Like.objects.get(user=user_id, secret=secret_id)
        messages.error(request, "You already liked this.")
    except (Like.DoesNotExist):
        Like.objects.create(user=user_id, secret=secret_id)
    return redirect(reverse('secrets:secrets_recent'))

def unlike(request, id):
    secret_id = Secret.objects.get(id=id)
    user_id = User.objects.get(id=request.session['id'])
    Like.objects.filter(user=user_id, secret=secret_id).delete()
    return redirect(reverse('secrets:secrets_recent'))