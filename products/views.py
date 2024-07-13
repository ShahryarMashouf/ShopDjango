from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Cart, CartItem, UserComments
from .forms import AddToCartForm, CommentForm
from django.http import HttpResponse, JsonResponse
 

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def add_to_cart(request):
    return render(request, 'product_details.html')

def product_details(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'product_details.html', {'product': product})

def form_view(request):
    form = CommentForm()
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            uc = UserComments(
                first_name = cd['first_name'],
                last_name = cd['last_name'],
                comment = cd['comment'],
                
            )
            uc.save()
            return JsonResponse({
                'message': 'success'
            })
    return render(request, 'blog.html', {'form': form})