from django.shortcuts import render
from django.http import HttpResponse
from . models import Product

def index (request):
    all_product = Product.objects.all()
    params = {'products' : all_product}
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
