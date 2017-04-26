from django.conf.urls import url
from orders import views

urlpatterns = [
	url(r'^openorders', views.openorders, name='openorders'),
]
