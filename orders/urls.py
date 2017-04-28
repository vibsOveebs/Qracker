from django.conf.urls import url
from orders import views

urlpatterns = [
	url(r'^myorders', views.myorders, name='myorders'),
    url(r'^openrequests', views.openrequests, name='openrequests'),
    url(r'^pickupitem', views.pickupitem, name='pickupitem'),
    url(r'^delivererexchange', views.delivererexchange, name='delivererexchange'),
    url(r'^recipientexchange', views.recipientexchange, name='recipientexchange'),
    url(r'^telereport', views.telereport, name='telereport'),
]
