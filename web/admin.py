from django.contrib import admin
from .models import Product, Cart
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price")


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):

    class Meta:
        model = Cart
        fields = '__all__'
