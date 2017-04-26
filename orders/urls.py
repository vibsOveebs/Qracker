from django.conf.urls import url
from orders import views

urlpatterns = [
	url(r'^openrequests', views.openrequests, name='openrequests'),
	url(r'^pickupitem', views.pickupitem, name='pickupitem'),
]
