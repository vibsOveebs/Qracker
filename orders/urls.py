from django.conf.urls import url
from orders import views

urlpatterns = [
    url(r'^open', views.open_orders, name='open_orders'),
]
