from random import choice, choices
from django import forms

class CustomerForm(forms.Form):
    name = forms.CharField(label="name", max_length=100)
    email = forms.EmailField(label="email")


