from django import forms
from menu.models import Item
from datetime import datetime
from userprofile.models import UserProfile


class AddItemForm(forms.ModelForm):
    name=forms.CharField(help_text="Please enter the Item name: ",max_length=128,required=True)
    food_or_drink=forms.ChoiceField(choices=(
        ("Food","Food"),
        ("Drink","Drink")))
    is_breakfast=forms.BooleanField(help_text = 'Breakfast Item?', required=False)
    is_lunch=forms.BooleanField(help_text = 'Lunch Item?', required=False)
    price=forms.DecimalField(help_text="Please enter the price: ", min_value=0,required=True)
    supplier = forms.ModelChoiceField(queryset=UserProfile.objects.filter(supplier_flag__exact=True))

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

class BrowseForm(forms.Form):
    RESTAURANT_CHOICES = (
        ('Starbucks', 'Starbucks'),
        ('McDonalds', 'McDonalds'),
        ('TacoBell', 'TacoBell'),
    )
    FOOD_OR_DRINK_CHOICES = (
        ('Food', 'Food'),
        ('Drink', 'Drink'),
    )
    BREAKFAST_OR_LUNCH_CHOICES = (
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch')
    )

    restaurant_name = forms.ChoiceField(choices = RESTAURANT_CHOICES, label='Restauarnt', initial='', widget=forms.Select(), required = True)
    food_or_drink = forms.MultipleChoiceField(choices = FOOD_OR_DRINK_CHOICES, label='Food or Drink', widget=forms.CheckboxSelectMultiple(), required = True)
    breakfast_or_lunch = forms.MultipleChoiceField(choices = BREAKFAST_OR_LUNCH_CHOICES, label='Breakfast or Lunch', widget=forms.CheckboxSelectMultiple(), required = True)
