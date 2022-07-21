from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('registration/', views.submitForm, name = 'submitForm'),
    #path('registration/complete/', views.formComplete, name = 'formComplete'),
    #path('<int:user_id>/registration/', views.submitForm, name = 'submitForm'),
    #path('<int:user_id>/registration/complete/', views.formComplete, name = 'formComplete')
]