from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from timeit import default_timer

def shop_index(request: HttpRequest):
    products = [
        ('Laptop', 999),
        ('Desktop', 1999),
        ('Smartphone', 2999)
    ]
    context ={
        "time_running": default_timer(),
        "product" : products,
    }

    return render(request, 'shopapp/shop-index.html')
# Create your views here.
