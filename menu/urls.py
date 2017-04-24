from django.conf.urls import url
from menu import views

urlpatterns = [
    url(r'^additem', views.add_menu_item, name='additem'),
    url(r'^search', views.search, name='search'),
    url(r'^mcdonalds', views.add_order_mcdonalds, name='mcdonalds'),
    url(r'^tacobell', views.add_order_tacobell, name='tacobell'),
    url(r'^browse', views.browse, name='browse'),
    url(r'^browseresults', views.browseresults, name='browseresults')
]
