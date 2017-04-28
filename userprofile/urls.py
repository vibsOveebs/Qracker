from django.conf.urls import url
from userprofile import views

urlpatterns = [
    url(r'^login', views.user_login, name='login'),
    url(r'^logout', views.user_logout, name='logout'),
    url(r'^register', views.register, name='register'),
    url(r'^viewprofile', views.view_current_profile, name='viewprofile'),
    url(r'^addfunds', views.addfunds, name='addfunds'),
]
