from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'tmnt/index.html')

def ninjas(request):
    turtle = 'tmnt.png'
    context = {
        'turtle': turtle
    }
    return render(request, 'tmnt/ninja.html', context)

def turtles(request, id):
    if id == 'blue':
        turtle = 'leonardo.jpg'
        context = {
            'turtle': turtle
        }
    elif id == 'purple':
        turtle = 'donatello.jpg'
        context = {
            'turtle': turtle
        }
    elif id == 'orange':
        turtle = 'michelangelo.jpg'
        context = {
            'turtle': turtle
        }
    elif id == 'red':
        turtle = 'raphael.jpg'
        context = {
            'turtle': turtle
        }
    else:
        turtle = 'notapril.jpg'
        context = {
            'turtle': turtle
        }
    return render(request, 'tmnt/ninja.html', context)