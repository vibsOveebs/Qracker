from django import forms
from menu.models import Order
from datetime import datetime

class McDonaldsOrderForm(forms.ModelForm):
	user_name = forms.CharField(help_text="Please enter your name: ", max_length=128, required=True)
	item_name = forms.ChoiceField(choices=(
		("Hash Brown", "Hash Brown"), 
		("Coffee", "Coffee"), 
		("Egg McMuffin", "Egg McMuffin"), 
		("Sausage", "Sausage")))
	restaurant_name = forms.CharField(widget=forms.HiddenInput(), initial='McDonalds')
	creation_time = forms.DateTimeField(widget=forms.HiddenInput(), initial=datetime.now())

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
	creation_time = forms.DateTimeField(widget=forms.HiddenInput(), initial=datetime.now())

    # An inline class to provide additional information on the form.
	class Meta:
		# Provide an association between the ModelForm and a model 
		model = Order
		fields = ('user_name', 'item_name', 'restaurant_name', 'creation_time')
