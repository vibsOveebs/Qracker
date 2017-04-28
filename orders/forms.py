from datetime import datetime
from django import forms
from orders.models import Transaction
from random import randint


# random code generator
def generate_code():
    return randint(0,9999)


# Partial Initiate Form
class PartialInitiateForm(forms.ModelForm):

    # item quantity choices
    QUANTITY_CHOICES = (
        (1, '1'), 
        (2, '2'), 
        (3, '3'), 
        (4, '4'), 
        (5, '5'),
    )

    # pickup location choics
    LOC_CHOICES = (
        ('Stairs', 'Stairs'), 
        ('Aquarium', 'Aquarium'), 
        ('Seal', 'Seal'),
    )

    creation_time = forms.DateTimeField(initial=datetime.now, widget=forms.HiddenInput())
    pickup_loc = forms.ChoiceField(choices=LOC_CHOICES, help_text="Please select a pickup location: ")
    quantity = forms.ChoiceField(choices=QUANTITY_CHOICES, help_text="Please select a quantity: ")
    tip = forms.DecimalField(help_text="Please enter a tip amount")
    code = forms.IntegerField(widget=forms.HiddenInput(), initial=generate_code)

    class Meta:
        model = Transaction
        fields = ('creation_time', 'pickup_loc', 'quantity', 'tip', 'code')


# Open Orders Form
class OpenOrdersForm(forms.ModelForm):
    class Meta:
        model=Transaction
        fields=('creation_time', 'pickup_loc', 'item', 'quantity')

