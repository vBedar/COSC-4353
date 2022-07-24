from django.urls import path
from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.home, name="home"),         #views.home will open the home function in views.py. When the user will request the home page, url'', we will call function home
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('accountcreated', views.accountcreated, name="accountcreated"),
    # #path('', views.index, name='index'),
    # path('registration/', views.submitForm, name = 'submitForm'),
    # path('registration/complete/', views.formComplete, name = 'formComplete'),
    # path('<int:user_id>/registration/', views.submitForm, name = 'submitForm'),
    # path('<int:user_id>/registration/complete/', views.formComplete, name = 'formComplete'),
    
    #path('', views.index, name='index'),
    path('quote/', views.submitFuelQuote, name='submitFuelQuote'),
    path('quote/complete/', views.fuelQuoteComplete, name='fuelQuoteComplete'),

 

    #path('registration/', views.submitForm, name = 'submitForm'),
    #path('registration/complete/', views.formComplete, name = 'formComplete'),
    path('<int:user_id>/QuoteHistory/', views.fuelHist, name="fuelHist"),
    path('<int:user_id>/editClient/', views.submitCliForm, name = 'submitCliForm'),
    path('<int:user_id>/editClient/complete/', views.formCliComplete, name = 'formCliComplete')
]