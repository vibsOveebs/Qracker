from django.conf.urls import url
from userprofile import views

urlpatterns = [
    url(r'^register', views.register, name='register'),
]
