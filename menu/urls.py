from django.conf.urls import url
from menu import views

urlpatterns = [
    url(r'^additem', views.add_menuitem, name='additem'),
    url(r'^search', views.search, name='search'),
    url(r'^tacobell', views.add_order_tacobell, name='tacobell'),
]
