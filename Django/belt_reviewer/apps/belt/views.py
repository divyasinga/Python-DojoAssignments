from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.db.models import Count
from django.core.urlresolvers import reverse
from .models import *
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'belt/index.html')

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['confirm']
        if User.objects.validate(email) and User.objects.validpw(password) and password == confirm:
            try:
                hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
                User.objects.create(email=email, password=hashed, first_name=first_name, last_name=last_name)
                request.session['user'] = first_name
                user = User.objects.get(email=email)
                request.session['id'] = user.id
                return redirect(reverse('reviewer:reviewer_recent'))
            except:
                messages.error(request, "User already exists.")
                return redirect(reverse('reviewer:reviewer_index'))
        if User.objects.validate(email) == False:
            messages.error(request, "Invalid email!")

        if User.objects.validpw(password) == False:
            messages.error(request, "Invalid password. Must contain one uppercase, one lowercase, and one number.")
        if password != confirm:
            messages.error(request, "Passwords do not match.")
    return redirect('reviewer:reviewer_index')

def login(request):
    if request.method == 'POST':
        loginemail = request.POST['user_email']
        loginpw = request.POST['user_pw'].encode()
        user = User.objects.get(email=loginemail)
        if bcrypt.hashpw(loginpw, user.password.encode()) == user.password.encode():
            request.session['user'] = user.first_name
            request.session['id'] = user.id
            return redirect(reverse('reviewer:reviewer_recent'))
        else:
            messages.error(request, "Invalid username or password.")
    return redirect(reverse('reviewer:reviewer_index'))

def recent(request):
    if 'id' in request.session:
        context = {
            'reviews': Review.objects.all().order_by('-created_at')[:3],
            'books': Book.objects.all().order_by('title'),
        }
        return render(request, 'belt/recent.html', context)
    else:
        return redirect(reverse('reviewer:reviewer_index'))

def post(request):
    if 'id' in request.session:
        context = {
            'authors': Author.objects.all()
        }
        return render(request, 'belt/post.html', context)
    else:
        return redirect(reverse('reviewer:reviewer_index'))

def submit(request):
    if 'id' in request.session:
        if request.method == "POST":
            if request.POST['author_selector']:
                author = request.POST['author_selector']
            else:
                author = request.POST['author']
                Author.objects.create(name=author)
            title = request.POST['title']
            review = request.POST['review_text']
            rating = int(request.POST['rating'])
            bookauthor = Author.objects.get(name=author)
            try:
                Book.objects.get(title=title)
            except (Book.DoesNotExist):
                Book.objects.create(title=title, author=bookauthor)
            book = Book.objects.get(title=title)
            Author.objects.filter(name=author).update(bookauthored=book)
            user = User.objects.get(id=request.session['id'])
            Review.objects.create(review_text=review, rating=rating, book=book, reviewer=user)
            return redirect(reverse('reviewer:reviewer_recent'))
    else:
        return redirect(reverse('reviewer:reviewer_index'))
    

def book(request, id):
    if 'id' in request.session:
        context = {
            'book': Book.objects.get(id=id),
            'reviews': Review.objects.filter(book=id)
        }
        return render(request, 'belt/books.html', context)
    else:
        return redirect(reverse('reviewer:reviewer_index'))

def user(request, id):
    if 'id' in request.session:
        context = {
            'user': User.objects.get(id=id),
            'reviews': Review.objects.filter(reviewer=id),
        }
        return render(request, 'belt/user.html', context)
    else:
        return redirect(reverse('reviewer:reviewer_index'))
    

def logout(request):
    request.session.clear()
    return redirect(reverse('reviewer:reviewer_index'))
