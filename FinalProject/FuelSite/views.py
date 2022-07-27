from django.shortcuts import render, get_object_or_404, redirect



# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import fuelQuote
from .forms import fuelQuoteForm
from .models import Client
from .forms import clientForm
from .models import User

#from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
#from cryptography.fernet import Fernet

#Dhruvs Views


#key = Fernet.generate_key()

def home(request):
    #return HttpResponse("hello I am working")
    return render(request, "authentication/login.html")


def signup(request):

    if request.method == "POST":
        #username = request.POST.get('username')
        username = request.POST['username']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        #we will register this user in the backend/ database

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username")
            # return redirect('home')
            return HttpResponse("Username already exist! Please reload and try again")
        
        if len(pass1)<2:
            messages.error(request, "Password is too short")
            return HttpResponse("Password is too short! Please reload and try again")
        
        if len(username)>15:
            messages.error(request, "Username must be under 15 characters")
            # return redirect('home')
            return HttpResponse("Username must be under 15 characters! Please reload and try again")
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't match!")
            # return redirect('home')
            return HttpResponse("The passwords didn't match! Please reload and try again")
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!")
            # return redirect('home')
            return HttpResponse("Username must be Alpha-Numeric! Please reload and tray again")

        # myuser = User.objects.create_user(username, email=None, password=pass1)

        # myuser.save()

        user_object = User()
        user_object.username = username

        new_string = ""

        for i in range(len(pass1)):
            char = pass1[i]
            char_value = ord(char)
            new_char_value = char_value + 3
            new_char = chr(new_char_value)
            new_string = new_string + new_char




        user_object.password = new_string
        
        user_object.save()


        #making a new client object that corresponds with User
        new_Client = Client.objects.create(user=user_object)
        new_Client.save()

        messages.success(request, "Your Account has been successfully created.")

        return redirect('home')

    return render(request, "authentication/registration.html")


def signin(request):

    if request.method == 'POST':
        user_username = request.POST['username']
        pass1 = request.POST['pass1']

        # user = authenticate(username=username, password=pass1)

        # if user is not None:
        #     login(request, user)
        #     return redirect('accountcreated')
        #     #user will log into the client profile page
        #     #return HttpResponse("you are successfully logged in")

        if User.objects.filter(username=user_username).first() is not None:
            
            encrypted_password = User.objects.get(username=user_username)

            new_string = ""

            for i in range(len(encrypted_password.password)):
                char = encrypted_password.password[i]
                char_value = ord(char)
                new_char_value = char_value - 3
                new_char = chr(new_char_value)
                new_string = new_string + new_char


            if new_string == pass1:
                #return redirect('accountcreated')
                return HttpResponseRedirect('%d/QuoteHistory'% encrypted_password.id)
            else:
                 return HttpResponse("Bad Credentials. Please reload and Try again")

        else:
            messages.error(request, "Bad Credentials")
            return redirect('home')
            #return HttpResponse("you are successfully logged in")
            #return HttpResonse("Bad Credentials, please reload the page and try again")

    return render(request, "authentication/login.html")

def accountcreated(request):
    return render(request, "authentication/successfullogin.html")




#Victoria's Views

def formCliComplete(request, user_id):
    return HttpResponse("Form Submitted, Thanks!")

def submitCliForm(request, user_id):
    #client_detail = get_object_or_404(Client, pk=user_id)
    user_detail = get_object_or_404(User, pk=user_id)
    client_detail = Client.objects.get(user=user_detail)
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
            return HttpResponseRedirect('/%d/QuoteHistory'% user_id) 
            #return HttpResponseRedirect(reverse('formCliComplete', args = (user.id)))

    else:
        form = clientForm()

    context = {
        'form': form,
        'client_detail': client_detail,
    }

    return render(request, 'ClientForm.html', context)    

def fuelHist(request, user_id):
    #data = fuelQuote.objects.get(user=user_id)
    # f = {
    #     "quote_num":data
    # }
    # return render_to_response('FuelQuoteHist.html', {'data',data})
    context = {
        'user_id': user_id,
    }
    return render(request, 'FuelQuoteHist.html', context)




#Kevin's Views

def index(request):
    #return render(request, 'FuelQuoteForm.html')
    return HttpResponseRedirect('quote/')

def fuelQuoteComplete(request, user_id):
    return HttpResponse('Fuel Quote Form Submitted Successfully')

def submitFuelQuote(request, user_id):
    fq = fuelQuote()
    if request.method == 'POST':
        form = fuelQuoteForm(request.POST)
        if form.is_valid():
            fq.gallonsRequested = form.cleaned_data['gallons_requested']
            fq.deliveryDate = form.cleaned_data['delivery_date']
            fq.deliveryAddress = form.cleaned_data['delivery_address']
            fq.suggestedPrice = form.cleaned_data['suggested_price']
            fq.totalAmountDue = form.cleaned_data['total_amount_due']
            fq.save()  
            return HttpResponseRedirect('complete/')
            #return HttpResponse('Fuel Quote Form Submitted Successfully')
    #return HttpResponse('SKIPPED REQUEST.METHOD')

    else:   #if GET (or anything other method)
        form = fuelQuoteForm()

    context = {
        'form': form,
        'fq': fq,
    }

    return render(request, 'FuelQuoteForm.html', context)
        
         