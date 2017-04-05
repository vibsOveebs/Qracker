from django import forms
from menu.models import Order

class McDonaldsOrderForm(forms.ModelForm):
	user_id = forms.IntegerField(help_text="Please enter your user id: ", required=True)
	item_name = forms.ChoiceField(choices=(
		("Hash Brown", "Hash Brown"), 
		("Coffee", "Coffee"), 
		("Egg McMuffin", "Egg McMuffin"), 
		("Sausage", "Sausage")))
	restaurant_name = forms.CharField(widget=forms.HiddenInput(), initial='McDonalds')

    # An inline class to provide additional information on the form.
	class Meta:
		# Provide an association between the ModelForm and a model 
		model = Order
		fields = ('user_id', 'item_name', 'restaurant_name')

class TacoBellOrderForm(forms.ModelForm):
	user_id = forms.IntegerField(help_text="Please enter your user id: ", required=True)
	item_name = forms.ChoiceField(choices=(
		("Taco", "Taco"),
		("Burrito", "Burrito"), 
		("Crunch Wrap", "Crunch Wrap"), 
		("Baja Blast", "Baja Blast")))
	restaurant_name = forms.CharField(widget=forms.HiddenInput(), initial='Taco Bell')

    # An inline class to provide additional information on the form.
	class Meta:
		# Provide an association between the ModelForm and a model 
		model = Order
		fields = ('user_id', 'item_name', 'restaurant_name')
