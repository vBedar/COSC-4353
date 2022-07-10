from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="home"),         #views.home will open the home function in views.py. When the user will request the home page, url'', we will call function home
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('accountcreated', views.accountcreated, name="accountcreated")
]
