from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from timeit import default_timer

def shop_index(request: HttpRequest):
    products = [
        ('Laptop', 999),
        ('Desktop', 1999),
        ('Smartphone', 2999)
    ]
    context = {
        "time_running": default_timer(),
        "products" : products,
    }

    return render(request, 'shopapp/shop-index.html', context = context)


def groups_list(request: HttpRequest):
    context = {
        "groups": Group.objects.prefetch_related("permissions").all()

    }
    return render(request, "shopapp/groups_list.html", context=context)