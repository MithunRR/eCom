from django.contrib import admin
from . models import Product, CartItem, Contact, Order, Career

# Register your models here.

admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(Career)


