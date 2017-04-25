from django import forms
from orders.models import Transaction
from datetime import datetime
from userprofile.models import UserProfile
from django.contrib.auth.models import User



class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('creation_time', 'delivery_time', 'pickup_loc', 'item', 'quantity', 'code_word',
        	'initiates', 'delivers', 'timeliness', 'friendliness', 'responsetime', 'text_feedback')
