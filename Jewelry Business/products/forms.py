from asyncio.windows_events import NULL
from email.policy import default
from queue import Empty
from random import choice, choices
from django import forms

class FilteredForm(forms.Form):
    minprice = forms.IntegerField(initial=0, label="minprice")
    maxprice = forms.IntegerField(initial=10000, label="maxprice")
    color = forms.ChoiceField(label="color", choices=[('Any','Any'), ('Black', 'Black'), ('Gold', 'Gold'), ('Copper', 'Copper'), ('Silver', 'Silver'), ('Brown', 'Brown')])
    jewelrytype = forms.ChoiceField(label="jewelrytype", choices=[('Any','Any'), ('Earring', 'Earring'), ('Ring', 'Ring'), ('Anklet', 'Anklet'), ('Necklace', 'Necklace'), ('Bracelet', 'Bracelet'), ('Hairclip', 'Hairclip')])


