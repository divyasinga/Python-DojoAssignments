from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import Course, Enrollment
from ..loggy.models import User

# Create your views here.
def index(request):
    context = {
        'courses': Course.objects.all(),
    }
    return render(request, 'courses/index.html', context)

def coursesubmission(request):
    if request.method == 'POST':
        Course.objects.create(name=request.POST['coursename'], description=request.POST['coursedesc'])
        return redirect(reverse('courses:course_index'))

def deletecourse(request, id):
    context = {
        'courses': Course.objects.filter(id=id)
    }
    return render(request, 'courses/delete.html', context)

def confirmdelete(request, id):
    if request.method == 'POST':
        Course.objects.filter(id=id).delete()
        return redirect(reverse('courses:course_index'))

def assignment(request):
    context = {
        'courses': Course.objects.all(),
        'users': User.objects.all(),
        'enrolled': Enrollment.objects.all(),
    }
    return render(request, 'courses/assignment.html', context)

def assign_submit(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.POST['user_selector'])
        course = Course.objects.get(id=request.POST['course_selector'])
        Enrollment.objects.create(course_enrolled=course, user_student=user)
    return redirect(reverse('courses:assignment'))
