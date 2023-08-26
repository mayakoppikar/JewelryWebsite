from django.shortcuts import render
from .forms import CustomerForm
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
import json
from products.models import *
from django.contrib.auth import login, authenticate
from django.views import generic



def customerfill(request):

    
    
        if request.method == 'POST':
            customer_form = CustomerForm(request.POST)
            if customer_form.is_valid():
                name = customer_form.cleaned_data.get("name")
                email = customer_form.cleaned_data.get("email")

              

                Customer.objects.create(
                user = request.user,
                name = name,
                email = email,
           
            )
            
            return render(request, 'home/index.html', {})


        form = CustomerForm()
        return render(request, 'home/customer.html', {'customerform': form})

    



# Create your views here.

class SignupView(CreateView):

    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = '/customer'

    def form_valid(self, form):
        to_return = super().form_valid(form)
        user = authenticate(
             username=form.cleaned_data["username"],
            password=form.cleaned_data["password1"],
        )
        login(self.request, user)
        return to_return



class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
             return redirect('/')
       
        return super().get(request, *args, **kwargs)

     

    
class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'



def home(request):
    return render(request, 'home/index.html', {})

def about(request):
    return render(request, 'home/about.html', {})


