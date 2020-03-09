from django.contrib import admin
from .models import *

admin.site.register(Brand)
admin.site.register(Category)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','brand','category','image']


admin.site.register(Product, ProductAdmin)

# Register your models here.
