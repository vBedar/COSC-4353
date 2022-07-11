from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .models import fuelQuote
from .forms import fuelQuoteForm

# Create your views here.

def index(request):
    return render(request, 'FuelQuoteForm.html')

def fuelQuoteComplete(request):
    return HttpResponse('Fuel Quote Form Submitted Successfully complete')

def submitFuelQuote(request):
    fq = fuelQuote
    if request.method == 'POST':
        form = fuelQuoteForm(request.POST)
        if form.is_valid():
            fq.gallonsRequested = form.cleaned_data['gallons_requested']
            fq.deliveryDate = form.cleaned_data['delivery_date']
            fq.deliveryAddress = form.cleaned_data['delivery_address']
            fq.suggestedPrice = form.cleaned_data['suggested_price']
            fq.totalAmountDue = form.cleaned_data['total_amount_due']
            #fq.save()
            #return redirect('fuelQuoteComplete')
            return HttpResponse('Fuel Quote Form Submitted Successfully')
    #return HttpResponse('SKIPPED REQUEST.METHOD')

    else:   #if GET (or anything other method)
        form = fuelQuoteForm()

    return render(request, 'FuelQuoteForm.html', {'form': form})
        
         


