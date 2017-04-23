from django import forms
from menu.models import Order, Item
from datetime import datetime

class additemform(forms.ModelForm):
    name=forms.CharField(help_text="Please enter the Item name: ",max_length=128,required=True)
    food_or_drink=forms.ChoiceField(choices=(
        ("Food","Food"),
        ("Drink","Drink")))
    is_breakfast=forms.BooleanField(help_text = 'Breakfast Food?', required=False)
    is_lunch=forms.BooleanField(help_text = 'Lunch Food?', required=False)
    price=forms.DecimalField(help_text="Please enter the price: ",min_value=0,required=True)

    class Meta:
        model = Item
        exclude = ['supplier', 'promo_flag']

    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user')
        super(ReviewForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        inst = super(ReviewForm, self).save(commit=False)
        inst.author = self._user
        if commit:
            inst.save()
            self.save_m2m()
        return inst

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
