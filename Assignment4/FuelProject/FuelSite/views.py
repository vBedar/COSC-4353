from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .models import Client
from .forms import clientForm

def index(request):
    #return HttpResponse()

# def formComplete(request):
#     return HttpResponse("Form Submitted, Thanks!")

# def submitForm(request):
#     clientregistration = Client
#     if request.method == 'POST':
#         form = clientForm(request.POST)
#         if form.is_valid():
#             clientregistration.name = form.cleaned_data['full_name']
#             clientregistration.stAddress1 = form.cleaned_data['address_1']
#             clientregistration.stAddress2 = form.cleaned_data['address_2']
#             clientregistration.city = form.cleaned_data['city']
#             clientregistration.state = form.cleaned_data['state']
#             clientregistration.zip = form.cleaned_data['zipcode']
#             #clientregistration.save()
#             return HttpResponseRedirect('complete/')

#     else:
#         form = clientForm()

#     return render(request, 'cForm/ClientForm.html', {'form': form})    
