from django.urls import path
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="home"),         #views.home will open the home function in views.py. When the user will request the home page, url'', we will call function home
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('accountcreated', views.accountcreated, name="accountcreated"),

    
    path('<int:user_id>/quote/', views.submitFuelQuote, name='submitFuelQuote'),
    path('<int:user_id>/quote/complete/', views.fuelQuoteComplete, name='fuelQuoteComplete'),


    path('<int:user_id>/QuoteHistory/', views.fuelHist, name="fuelHist"),
    path('<int:user_id>/editClient/', views.submitCliForm, name = 'submitCliForm'),
    path('<int:user_id>/editClient/complete/', views.formCliComplete, name = 'formCliComplete')
]