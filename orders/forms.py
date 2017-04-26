from django import forms
from orders.models import Transaction
from datetime import datetime
from userprofile.models import UserProfile
from django.contrib.auth.models import User
from random import randint

def generate_code():
    return randint(0,9999)

class PartialInitiateForm(forms.ModelForm):
    QUANTITY_CHOICES = (
        (1, '1'), 
        (2, '2'), 
        (3, '3'), 
        (4, '4'), 
        (5, '5'),
    )
    LOC_CHOICES = (
        ('Stairs', 'Stairs'), 
        ('Aquarium', 'Aquarium'), 
        ('Seal', 'Seal'),
    )
    creation_time = forms.DateTimeField(initial=datetime.now, widget=forms.HiddenInput())
    pickup_loc = forms.ChoiceField(choices=LOC_CHOICES, help_text="Please select a pickup location: ")
    quantity = forms.ChoiceField(choices=QUANTITY_CHOICES, help_text="Please select a quantity: ")
    code = forms.IntegerField(widget=forms.HiddenInput(), initial=generate_code)

    class Meta:
        model = Transaction
        fields = ('creation_time', 'pickup_loc', 'quantity', 'code')

class OpenOrdersForm(forms.ModelForm):
    class Meta:
        model=Transaction
        fields=('creation_time', 'pickup_loc', 'item', 'quantity')