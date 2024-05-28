from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Cart, CartItem
from .forms import AddToCartForm
from django.http import HttpResponse

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def add_to_cart(request):
    return render(request, 'product_details.html')

def product_details(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'product_details.html', {'product': product})