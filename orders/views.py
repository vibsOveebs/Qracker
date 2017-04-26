from django.shortcuts import render
from orders.forms import showorderform
from orders.models import Transaction

from qracker.views import index

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.db.models import Q

def pickorder(request):
    form = showorderform()

    if request.method=='POST':
        form=showorderform(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return (request)
        else:
            print(form.errors)

    return render(request, "menu/pickorder.html", {'form': form})