from django.urls import path
from . import views

urlpatterns = [
    path('products', views.list, name='products.show'),
    path('filteredproducts', views.filter),
    path('products/<str:pr>', views.detail),
    path('cart', views.cart, name='products.cart'),
    path('checkout', views.checkout, name='products.checkout'),
    path('update_item/', views.updateItem, name='products.update_item'),
    path('process_order/', views.processOrder, name='products.process_order'),




]

