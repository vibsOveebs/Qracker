from django.shortcuts import render
from orders.models import Transaction

from qracker.views import index

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.db.models import Q

def openorders(request):
    context_dict = {}

    transactions = Transaction.objects.filter(delivery_time__isnull=True)
    context_dict['transactions'] = transactions

    return render(request, "orders/openorders.html", context_dict)