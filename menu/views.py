from django.shortcuts import render
from menu.forms import AddItemForm, BrowseForm, SearchForm
from menu.models import Item


def add_menu_item(request):
    form = AddItemForm()

    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return success(request)
        else:
            print(form.errors)

    return render(request, "menu/add_item.html", {'form': form})


def success(request):
    return render(request, 'menu/success.html')


# search view
def search(request):
    form = SearchForm()

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            return results(request)
        else:
            print(form.errors)

    return render(request, 'menu/search.html', {'form': form})


# results view
def results(request):
    # get search parameters
    searchstring = request.POST.get('searchstring')
    food_or_drink = request.POST.get('food_or_drink')
    is_breakfast = request.POST.get('is_breakfast')
    is_lunch = request.POST.get('is_lunch')

    # filter the Item set using search parameters
    results = Item.objects.filter(
        food_or_drink__exact=food_or_drink
    ).filter(
        is_breakfast__exact=is_breakfast
    ).filter(
        is_lunch__exact=is_lunch
    ).filter(
        name__icontains=searchstring
    ).order_by(
        '-promo_flag'
    )

    # ORDER RESULTS BY PROMO FLAG THEN BY POPULARITY

    context_dict = {'results': results}

    # render
    return render(request, 'menu/results.html', context_dict)


def browse(request):
    form = BrowseForm()
    return render(request, 'menu/browse.html', {'form': form})
