from django.shortcuts import render, redirect, HttpResponse
from .models import Course

# Create your views here.
def index(request):
    context = {
        'courses': Course.objects.all(),
    }
    return render(request, 'courses/index.html', context)

def coursesubmission(request):
    if request.method == 'POST':
        Course.objects.create(name=request.POST['coursename'], description=request.POST['coursedesc'])
        return redirect('/')

def deletecourse(request, id):
    context = {
        'courses': Course.objects.filter(id=id)
    }
    return render(request, 'courses/delete.html', context)

def confirmdelete(request, id):
    if request.method == 'POST':
        Course.objects.filter(id=id).delete()
        return redirect('/')
