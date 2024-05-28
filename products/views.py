from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Cart, CartItem
from .forms import AddToCartForm
from django.http import HttpResponse

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


# @login_required
def add_to_cart(request):
    print("kir")
    
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            product_id = form.cleaned_data['product_id']
            quantity = form.cleaned_data['quantity']
            product = get_object_or_404(Product, id=product_id)
            
            cart, created = Cart.objects.get_or_create(user=request.user)
            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
            if not created:
                cart_item.quantity += quantity
            else:
                cart_item.quantity = quantity
            cart_item.save()
            return redirect('index')
        else:
            return HttpResponse("Form is not valid")  # Debugging statement
    return HttpResponse("Request is not POST")  # Debugging statement
