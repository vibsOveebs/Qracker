from django.shortcuts import render

from django.http import HttpResponse

from menu.forms import McDonaldsOrderForm, TacoBellOrderForm, SearchForm
from menu.models import Item


def success(request):
    return render(request, 'menu/success.html')


def add_order_mcdonalds(request):
    form = McDonaldsOrderForm()

    # A HTTP POST?
    if request.method == 'POST':
        form = McDonaldsOrderForm(request.POST)
        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)
            # Now that the category is saved
            # We could give a confirmation message
            # But since the most recent category added is on the index page
            # Then we can direct the user back to the index page.
            return success(request)
        else:
            # The supplied form contained errors -
            # just print them to the terminal.
            print(form.errors)

    # Will handle the bad form, new form, or no form supplied cases.
    # Render the form with error messages (if any).
    return render(request, 'menu/add_order_mcdonalds.html', {'form': form})


def add_order_tacobell(request):
    form = TacoBellOrderForm()

    if request.method == 'POST':
        form = TacoBellOrderForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return success(request)
        else:
            print(form.errors)

    return render(request, 'menu/add_order_tacobell.html', {'form': form})


# search view
def search(request):
    form = SearchForm()

    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            searchstring = request.GET.get('searchstring')
            food_or_drink = request.GET.get('food_or_drink')
            is_breakfast = request.GET.get('is_breakfast')
            is_lunch = request.GET.get('is_lunch')

            results = Item.objects.filter(
                food_or_drink__exact=food_or_drink
            ).filter(
                is_breakfast__exact=is_breakfast
            ).filter(
                is_lunch__exact=is_lunch
            ).filter(
                name__icontains=searchstring
            )
            return render('menu/results.html', results)