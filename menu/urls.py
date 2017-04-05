from django.conf.urls import url
from menu import views

urlpatterns = [
	url(r'^mcdonalds', views.mcdonalds, name='mcdonalds'),
	url(r'^tacobell', views.tacobell, name='tacobell'),
]