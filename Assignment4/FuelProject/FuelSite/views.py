from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Client
from .forms import clientForm

def index(request):
    #return HttpResponse()
    #return HttpResponseRedirect('registration/')
    #return HttpResponseRedirect(reverse('submitForm'), args)

def formComplete(request):
    return HttpResponse("Form Submitted, Thanks!")

def submitForm(request, user_id):
    client_detail = get_object_or_404(Client, pk=user_id)
    if request.method == 'POST':
        form = clientForm(request.POST)
        if form.is_valid():
            client_detail.name = form.cleaned_data['full_name']
            client_detail.stAddress1 = form.cleaned_data['address_1']
            client_detail.stAddress2 = form.cleaned_data['address_2']
            client_detail.city = form.cleaned_data['city']
            client_detail.state = form.cleaned_data['state']
            client_detail.zip = form.cleaned_data['zipcode']
            client_detail.save()
            return HttpResponseRedirect('complete/') 
            #return HttpResponseRedirect(reverse('formComplete', args = (user.id)))

    else:
        form = clientForm()

    context = {
        'form': form,
        'client_detail': client_detail,
    }

    return render(request, 'ClientForm.html', context)    
