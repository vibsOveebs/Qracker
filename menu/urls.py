from django.conf.urls import url
from menu import views

urlpatterns = [
    url(r'^mcdonalds', views.add_order_mcdonalds, name='mcdonalds'),
    url(r'^tacobell', views.add_order_tacobell, name='tacobell'),
]
