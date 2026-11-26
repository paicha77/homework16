from django.shortcuts import render
from django.db.models import Q, F
from .models import Product

# aq Q
# | es aris OR, & es aris AND da ~ es aris ar akmayopilebs
def q_expression_1():
    products = Product.objects.filter(
        Q(price__gt=50) | Q(quantity__lt=10)
    )

    return products

def q_expression_2():
    products = Product.objects.filter(
        Q(name__icontains="phone") & Q(price__range=(100, 500))
    )

    return products

def q_expression_3():
    products = Product.objects.filter(
        ~Q(price__lt=200)
    )

    return products


# aq F
def f_expression_1():
    Product.objects.update(
        price=F('price') + 10
    )


def f_expression_2():
    products = Product.objects.filter(
        price__gt=F('quantity')
    )

    return products


def f_expression_3():
    Product.objects.update(
        quantity=F('quantity') + 1
    )