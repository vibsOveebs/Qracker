from django import forms
from django.contrib.auth.models import User
from menu.models import Item
from userprofile.models import UserProfile


# Add Item Form
class AddItemForm(forms.ModelForm):
    name=forms.CharField(help_text="Please enter the Item name: ",max_length=128,required=True)
    food_or_drink=forms.ChoiceField(choices=(
        ("Food","Food"),
        ("Drink","Drink")))
    is_breakfast=forms.BooleanField(help_text = 'Breakfast Item?', required=False)
    is_lunch=forms.BooleanField(help_text = 'Lunch Item?', required=False)
    price=forms.DecimalField(help_text="Please enter the price: ", min_value=0,required=True)
    supplier = forms.ModelChoiceField(queryset=User.objects.filter(id__in = UserProfile.objects.filter(supplier_flag__exact=True).values_list('user_id')))

    class Meta:
        model = Item
        exclude = ['promo_flag']


# Search Form
class SearchForm(forms.ModelForm):
    searchstring = forms.CharField(help_text= 'Item Name: ', max_length=128, required=False)
    food_or_drink = forms.ChoiceField(help_text='Select if Food or Drink',choices=(
        ('Food', 'Food'),
        ('Drink', 'Drink'),
    ), required=False)
    is_breakfast = forms.BooleanField(help_text='Breakfast?',initial=False, required=False)
    is_lunch = forms.BooleanField(help_text='Lunch?',initial=False, required=False)

    class Meta:
        model = Item
        fields = ('searchstring', 'food_or_drink', 'is_breakfast', 'is_lunch') 


# Browse Form
class BrowseForm(forms.ModelForm):
    restaurant_name = forms.ModelChoiceField(queryset=User.objects.filter(id__in = UserProfile.objects.filter(supplier_flag__exact=True).values_list('user_id')), required=True)
    is_food = forms.BooleanField(label='Food?', initial=False, required=False)
    is_drink = forms.BooleanField(label='Drink?', initial=False, required=False)
    is_breakfast = forms.BooleanField(label='Breakfast?', initial=False, required=False)
    is_lunch = forms.BooleanField(label='Lunch?', initial=False, required=False)

    class Meta:
        model = Item
        fields = ('restaurant_name', 'is_breakfast', 'is_lunch')


# Browse Results Form
class BrowseResultsForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'food_or_drink', 'is_breakfast', 'is_lunch', 'price', 'supplier')
