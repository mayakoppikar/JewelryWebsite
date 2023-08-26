from django.contrib import admin
from . import models
# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = ['jewelrytype', 'price', 'description', 'code', 'color', 'image']

admin.site.register(models.Products, ProductsAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'email']

admin.site.register(models.Customer, CustomerAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'date_ordered', 'complete', 'transaction_id']

admin.site.register(models.Order, OrderAdmin)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'order', 'quantity', 'date_added']

admin.site.register(models.OrderItem, OrderItemAdmin)

class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['customer', 'order', 'address', 'date_added']

admin.site.register(models.ShippingAddress, ShippingAddressAdmin)


