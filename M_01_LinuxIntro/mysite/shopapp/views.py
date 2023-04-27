from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, reverse
from timeit import default_timer
from .forms import ProductsForm

from .models import Product, Order
def shop_index(request: HttpRequest):
    products = [
        ('Laptop', 999),
        ('Desktop', 1999),
        ('Smartphone', 2999)
    ]
    context = {
        "time_running": default_timer(),
        "products": products,
    }

    return render(request, 'shopapp/shop-index.html', context=context)


def groups_list(request: HttpRequest):
    context = {
        "groups": Group.objects.prefetch_related("permissions").all()

    }
    return render(request, "shopapp/groups_list.html", context=context)


def products_list(request: HttpRequest):
    context = {
        "products" : Product.objects.all(),
    }
    return render(request, "shopapp/products-list.html", context=context)

def create_product(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ProductsForm(request.POST)
        if form.is_valid():

            form.save()
            url = reverse('shopapp:products_list')
            return redirect(url)
    else:


        form = ProductsForm()
    context = {
        'form': form,
    }

    return render(request, 'shopapp/create-product.html', context= context)


def orders_list(request: HttpRequest):
    context = {
        'orders': Order.objects.select_related("user").prefetch_related("products").all(),
    }
    return render(request, "shopapp/orders-list.html", context=context)
