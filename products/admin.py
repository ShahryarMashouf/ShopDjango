from . models import Product
from django.contrib import admin


class ProductAdmin(admin.ModelAdmin):
    list_display =  ('name','price','stock')
    


admin.site.register(Product,ProductAdmin)
