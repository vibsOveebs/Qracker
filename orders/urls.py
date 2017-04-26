from django.conf.urls import url
from orders import views

urlpatterns = [
    url(r'^openrequests', views.openrequests, name='openrequests'),
    url(r'^pickupitem', views.pickupitem, name='pickupitem'),
    url(r'^myrequests', views.myrequests, name='myrequests'),
    url(r'^mydeliveries', views.mydeliveries, name='mydeliveries'),
    url(r'^recipientexchange', views.recipientexchange, name='recipientexchange'),
]
