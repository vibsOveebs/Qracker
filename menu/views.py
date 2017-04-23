from django.shortcuts import render
from menu.forms import McDonaldsOrderForm, TacoBellOrderForm, additemform, BrowseForm, SearchForm
from menu.models import Item
from django.contrib.auth.decorators import user_passes_test


def add_menuitem(request):
    form = additemform(request.POST, user=request.user)

    if request.method == 'POST':
        form = additemform(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return success(request)
        else:
            print(form.errors)

    return render(request, "menu/add_item.html", {'form': form})


def success(request):
    return render(request, 'menu/success.html')


@user_passes_test(lambda u: Group.objects.get(name='customer') in u.groups.all())
def add_order_mcdonalds(request):
    form = McDonaldsOrderForm()

    # A HTTP POST?
    if request.method == 'POST':
        form = additemform(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return success(request)
        else:
            print(form.errors)

    return render(request, "menu/add_item.html", {'form': form})


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

    if request.method == 'POST':
        searchstring = request.POST.get('searchstring')
        food_or_drink = request.POST.get('food_or_drink')
        is_breakfast = request.POST.get('is_breakfast')
        is_lunch = request.POST.get('is_lunch')

        results = Item.objects.filter(
            food_or_drink__exact=food_or_drink
        ).filter(
            is_breakfast__exact=is_breakfast
        ).filter(
            is_lunch__exact=is_lunch
        ).filter(
            name__icontains=searchstring
        )
        return render(request, 'menu/results.html', results)


def browse(request):
    form = BrowseForm()
    return render(request, 'menu/browse.html', {'form': form})

