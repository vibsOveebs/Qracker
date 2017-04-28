from django.conf.urls import url
from userprofile import views

urlpatterns = [
    url(r'^login', views.user_login, name='login'),
    url(r'^logout', views.user_logout, name='logout'),
    url(r'^register', views.register, name='register'),
    url(r'^viewmyprofile', views.view_my_profile, name='viewmyprofile'),
    url(r'^viewotherprofile', views.view_other_profile, name='viewotherprofile'),
    url(r'^addfunds', views.addfunds, name='addfunds'),
]
