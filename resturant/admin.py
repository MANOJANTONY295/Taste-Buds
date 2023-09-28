from django.contrib import admin
from .models import Products, Categorys, CustomUser
# Register your models here.
admin.site.register(CustomUser),
admin.site.register(Categorys),
admin.site.register(Products),