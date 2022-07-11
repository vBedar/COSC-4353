from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('quote/', views.submitFuelQuote, name='submitFuelQuote'),
    path('quote/complete', views.fuelQuoteComplete, name='fuelQuoteComplete'),
]