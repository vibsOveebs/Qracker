from django.shortcuts import render
from menu.models import Order


def open_orders(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary
    # that will be passed to the template engine.
    order_list = Order.objects.order_by('-creation_time')
    context_dict = {'orders': order_list}
    # Render the response and send it back!
    return render(request, 'orders/open.html', context_dict)
