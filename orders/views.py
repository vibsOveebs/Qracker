from django.shortcuts import render
from orders.models import Transaction


# open requests view
def openrequests(request):

    # initialize context dictionary
    context_dict = {}

    # get unclaimed transactions
    transactions = Transaction.objects.filter(
        delivers__isnull=True)

    # update context dictionary
    context_dict['transactions'] = transactions

    # render
    return render(request, "orders/openrequests.html", context_dict)


# Pickup item button view
def pickupitem(request):

    # if pickup item has been submitted
    if request.method == 'GET':

        # get transaction id and print it
        transactionid = request.GET['transactionid']
        print(transactionid)

        # get transaction and print it
        transaction = Transaction.objects.get(id=transactionid)
        print(transaction)

        # set delivers to the current user
        transaction.delivers = request.user

        # save the form in the database
        transaction.save()

        # render success page
        return pickupsuccess(request)


# pickup success view
def pickupsuccess(request):
    return render(request, 'orders/pickupsuccess.html')


# My Requests view
def myrequests(request):

    # initialize context dictionary and grab userid
    context_dict = {}
    userid = request.user.id

    # find transactions that matches that userid
    transactions = Transaction.objects.filter(
        initiates__exact=userid).filter(
        delivery_time__isnull=True)

    # put transactions into the context dictionary
    context_dict['transactions'] = transactions

    #render
    return render(request, "orders/myrequests.html", context_dict)


# My Deliveries view
def mydeliveries(request):

    # initialize context dictionary and grab userid
    context_dict = {}
    userid = request.user.id

    # find transactions that matches that userid
    transactions = Transaction.objects.filter(
        delivers__exact=userid).filter(
        delivery_time__isnull=True)

    # put transactions into the context dictionary
    context_dict['transactions'] = transactions

    # render
    return render(request, "orders/mydeliveries.html", context_dict)
