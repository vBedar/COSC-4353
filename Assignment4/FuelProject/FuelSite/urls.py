from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('registration/', views.submitForm, name = 'submitForm'),
    # path('registration/complete/', views.formComplete, name = 'formComplete')
]