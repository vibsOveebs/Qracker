from django import forms
from menu.models import Item
from datetime import datetime
from userprofile.models import UserProfile
from django.contrib.auth.models import User

class AddItemForm(forms.ModelForm):
    name=forms.CharField(help_text="Please enter the Item name: ",max_length=128,required=True)
    food_or_drink=forms.ChoiceField(choices=(
        ("Food","Food"),
        ("Drink","Drink")))
    is_breakfast=forms.BooleanField(help_text = 'Breakfast Item?', required=False)
    is_lunch=forms.BooleanField(help_text = 'Lunch Item?', required=False)
    price=forms.DecimalField(help_text="Please enter the price: ", min_value=0,required=True)
    supplier = forms.ModelChoiceField(queryset=User.objects.filter(id = UserProfile.objects.filter(supplier_flag__exact=True).values_list('user_id')))

    class Meta:
        model = Item
        exclude = ['promo_flag']


# search form
class SearchForm(forms.ModelForm):
    searchstring = forms.CharField(max_length=128)
    food_or_drink = forms.ChoiceField(choices=(
        ('Food', 'Food'),
        ('Drink', 'Drink'),
    ))
    is_breakfast = forms.BooleanField(initial=False)
    is_lunch = forms.BooleanField(initial=False)

    class Meta:
        model = Item
        fields = ('searchstring', 'food_or_drink', 'is_breakfast', 'is_lunch') 

class BrowseForm(forms.ModelForm):
    restaurant_name = forms.ModelChoiceField(queryset=UserProfile.objects.filter(supplier_flag__exact=True), required=True)
    is_food = forms.BooleanField(initial=False, required=False)
    is_drink = forms.BooleanField(initial=False, required=False)
    is_breakfast = forms.BooleanField(initial=False, required=False)
    is_lunch = forms.BooleanField(initial=False, required=False)

    class Meta:
        model = Item
        fields = ('restaurant_name', 'is_breakfast', 'is_lunch')

class BrowseResultsForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'price', 'supplier')
