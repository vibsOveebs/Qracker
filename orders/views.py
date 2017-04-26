from django.shortcuts import render
from orders.models import Transaction

from qracker.views import index

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.db.models import Q

from menu.views import success

from datetime import datetime

def openrequests(request):
    context_dict = {}

    transactions = Transaction.objects.filter(delivers__isnull=True)
    context_dict['transactions'] = transactions

    return render(request, "orders/openrequests.html", context_dict)

def pickupitem(request):
    if request.method == 'GET':
        transactionid = request.GET['transactionid']
        print(transactionid)
        transaction = Transaction.objects.get(id=transactionid)
        print(transaction)
        transaction.delivers = request.user
        transaction.save()
        return pickupsuccess(request)

def pickupsuccess(request):
    return render(request, 'orders/pickupsuccess.html')

def orderitem(request):
    form = PartialInitiateForm();
    userid = request.user.id

    if request.method == 'GET':
        itemid = request.GET['itemid']
    elif request.method == 'POST':
        itemid = request.POST.get('itemid')
        form = PartialInitiateForm(request.POST)
        transaction = form.save(commit=False)
        transaction.initiates = User.objects.get(id=userid)
        transaction.item = Item.objects.get(id=itemid)
        transaction.save()
        print(form.errors)
        return success(request)

    return render(request, 'menu/orderitem.html', {'form': form, 'itemid' : itemid})