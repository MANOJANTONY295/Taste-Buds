from django.contrib import admin
from .models import Products, Categorys, CustomUser, Order #, OrderItem
# Register your models here.
admin.site.register(CustomUser),
admin.site.register(Categorys),
admin.site.register(Products),
#admin.site.register(OrderItem),
admin.site.register(Order),