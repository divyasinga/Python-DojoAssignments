from django.shortcuts import render, HttpResponse
from datetime import datetime

def index(request):
    context = {
        'somekey': datetime.now()
    }
    return render(request, 'timedisplay/page.html', context)