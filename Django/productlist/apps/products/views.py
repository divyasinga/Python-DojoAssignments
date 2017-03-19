from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import Product
# Create your views here.

def index(request):
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'products/index.html', context)

def new(request):
    return render(request, 'products/new.html')

def submit_new(request):
    if request.method == "POST":
        product_name = request.POST['product_name']
        product_desc = request.POST['product_desc']
        product_price = request.POST['product_price']
        Product.objects.create(name=product_name, description=product_desc, price=product_price)
        return redirect(reverse('products:product_index'))

def edit(request, id):
    context = {
        'product': Product.objects.filter(id=id)
    }
    return render(request, 'products/edit.html', context)

def submit_edit(request):
    if request.method == "POST":
        product_id = int(request.POST['product_id'])
        product_name = request.POST['product_name']
        product_desc = request.POST['product_desc']
        product_price = request.POST['product_price']
        Product.objects.filter(id=product_id).update(name=product_name, description=product_desc, price=product_price)
        return redirect(reverse('products:product_index'))

def show(request, id):
    context = {
        'product': Product.objects.filter(id=id)
    }
    return render(request, 'products/show.html', context)

def delete(request, id):
    context = {
        'product': Product.objects.filter(id=id)
    }
    return render(request, 'products/delete.html', context)

def submit_delete(request):
    if request.method == "POST":
        product_id = int(request.POST['product_id'])
        Product.objects.filter(id=product_id).delete()
        return redirect(reverse('products:product_index'))