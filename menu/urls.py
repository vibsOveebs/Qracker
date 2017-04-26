from django.conf.urls import url
from menu import views

urlpatterns = [
    url(r'^additem', views.add_menu_item, name='additem'),
    url(r'^search', views.search, name='search'),
    url(r'^browse', views.browse, name='browse'),
    url(r'^browseresults', views.browseresults, name='browseresults'),
    #url(r'^orderitem/(?P<itemid>[0-9]*)/?submit=', views.orderitem, name='orderitem'),
    url(r'^orderitem', views.orderitem, name='orderitem'),
]
