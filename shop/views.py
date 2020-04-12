from django.shortcuts import render
from django.http import HttpResponse
from . models import Product
from math import ceil

def index (request):
    products = Product.objects.all()
    print (products)
    n = len(products)
    nSlides = n//4 + ceil((n/4) - (n//4))
    params = {'no_of_slides' : nSlides, 'range' : range(1, nSlides), 'product' : products}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse('We Are At Contact')

def tracker(request):
    return HttpResponse('We Are At Tracker')

def search(request):
    return HttpResponse('We Are At Search')

def productview(request):
    return HttpResponse('We Are At Product View')

def checkout(request):
    return HttpResponse('We Are At Checkout')
