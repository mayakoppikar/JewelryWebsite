import json
from django.shortcuts import render
from .models import *
import datetime
from django.shortcuts import redirect
from django.views.generic import DetailView
from .forms import FilteredForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse

# Create your views here.

def list(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete= False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        cartItems = 0
        order = {'get_cart_total': 0, 'get_cart_items':0}


    all_products = Products.objects.all()
    context = {'prod':all_products,'cartItems': cartItems}
    return render(request, 'products/product_list.html', context)

def filter(request):
    if request.method == 'POST':
        filled_form = FilteredForm(request.POST)
        if filled_form.is_valid():
            jewelrytype = filled_form.cleaned_data.get("jewelrytype")
            minprice = filled_form.cleaned_data.get("minprice")
            color = filled_form.cleaned_data.get("color")
            maxprice = filled_form.cleaned_data.get("maxprice")
            if color == 'Any' and jewelrytype != 'Any':
                 filteredprods = Products.objects.filter(jewelrytype = jewelrytype, price__gte = minprice, price__lte = maxprice)
                 return render(request, 'products/product_list.html', {'prod': filteredprods})

            if color != 'Any' and jewelrytype == 'Any':
                 filteredprods = Products.objects.filter( price__gte = minprice, price__lte = maxprice, color= color)
                 return render(request, 'products/product_list.html', {'prod': filteredprods})
            if color == 'Any' and jewelrytype == 'Any':
                 filteredprods = Products.objects.filter( price__gte = minprice, price__lte = maxprice)
                 return render(request, 'products/product_list.html', {'prod': filteredprods})

            filteredprods = Products.objects.filter(jewelrytype = jewelrytype, price__gte = minprice, price__lte = maxprice, color = color)
            return render(request, 'products/product_list.html', {'prod': filteredprods})


    form = FilteredForm()
    return render(request, 'products/filter.html', {'filteredform': form})





def detail(request, pr):
    pdetail = Products.objects.filter(code = pr)
    return render(request, 'products/product_detail.html', {'product': pdetail})


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete= False)
        items = order.orderitem_set.all()
    else:
        return redirect('/login')
    context = {'items': items, 'order':order}
    return render(request, 'products/cart.html', context)

def checkout(request):
     if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete= False)
        items = order.orderitem_set.all()
     else:
        return redirect('/login')
     context = {'items': items, 'order':order}

     return render(request, 'products/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action', action)
    print('Prod', productId)

    customer = request.user.customer
    product = Products.objects.get(code = productId)
    order, created = Order.objects.get_or_create(customer = customer, complete= False)
    orderItem, created = OrderItem.objects.get_or_create(order = order, product= product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()


    return JsonResponse('Item was added', safe=False)



def processOrder(request):
    data = json.loads(request.body)

    transaction_id = datetime.datetime.now().timestamp()
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer = customer, complete= False)
    order.transaction_id = transaction_id
    order.complete = True
    order.save()

    ShippingAddress.objects.create(
            customer = customer,
            order = order,
            address = data['shipping']['address'],
            city = data['shipping']['city'],
            state = data['shipping']['state'],
            zipcode = data['shipping']['zipcode'],
        )
    

    return JsonResponse('payment complete', safe=False)







