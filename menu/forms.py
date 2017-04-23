from django import forms
from menu.models import Item
from datetime import datetime
from django.contrib.auth.models import User

class additemform(forms.ModelForm):
    supplier=forms.Foreignkey(User)
    name=forms.CharField(help_text="Please enter the Item name: ",max_length=128,required=True)
    FOOD_OR_DRINK_CHOICE=forms.ChoiceField(choices=(
        ("Food","Food"),
        ("Drink","Drink")))
    is_breakfast=forms.BooleanField(required=False)
    is_lunch=forms.BooleanField(required=False)
    Promo_flag=forms.BooleanField(required=False)
    price=forms.DecimalField(help_text="Please enter the price: ",min_value=0,required=True)

    class Meta:
        model=Item



class McDonaldsOrderForm(forms.ModelForm):
    user_name = forms.CharField(help_text="Please enter your name: ", max_length=128, required=True)
    item_name = forms.ChoiceField(choices=(
        ("Hash Brown", "Hash Brown"),
        ("Coffee", "Coffee"),
        ("Egg McMuffin", "Egg McMuffin"),
        ("Sausage", "Sausage")))
    restaurant_name = forms.CharField(widget=forms.HiddenInput(), initial='McDonalds')
    creation_time = forms.DateTimeField(widget=forms.HiddenInput(), initial=datetime.now)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Order
        fields = ('user_name', 'item_name', 'restaurant_name', 'creation_time')


class TacoBellOrderForm(forms.ModelForm):
    user_name = forms.CharField(help_text="Please enter your name: ", max_length=128, required=True)
    item_name = forms.ChoiceField(choices=(
        ("Taco", "Taco"),
        ("Burrito", "Burrito"),
        ("Crunch Wrap", "Crunch Wrap"),
        ("Baja Blast", "Baja Blast")))
    restaurant_name = forms.CharField(widget=forms.HiddenInput(), initial='Taco Bell')
    creation_time = forms.DateTimeField(widget=forms.HiddenInput(), initial=datetime.now)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Order
        fields = ('user_name', 'item_name', 'restaurant_name', 'creation_time')
