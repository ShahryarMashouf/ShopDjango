from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('add_to_cart/<str:product_id>/', views.product_details, name='product_details'),
    path('products/', views.index, name='products'),
]
