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


from django.contrib import messages
from django.contrib.auth import authenticate, login
from passlib.hash import pbkdf2_sha256

#Dhruvs Views




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

        # new_string = ""

        # for i in range(len(pass1)):
        #     char = pass1[i]
        #     char_value = ord(char)
        #     new_char_value = char_value + 3
        #     new_char = chr(new_char_value)
        #     new_string = new_string + new_char

        # user_object.password = new_string

        enc_password = pbkdf2_sha256.encrypt(pass1)
        user_object.password = enc_password
        
        user_object.save()


        #making a new client object that corresponds with User
        #new_Client = Client.objects.create(user=user_object)
        #new_Client.save()

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
            
            current_User = User.objects.get(username=user_username)

            # new_string = ""

            # for i in range(len(encrypted_password.password)):
            #     char = encrypted_password.password[i]
            #     char_value = ord(char)
            #     new_char_value = char_value - 3
            #     new_char = chr(new_char_value)
            #     new_string = new_string + new_char


            # if new_string == pass1:
            #     return redirect('accountcreated')
            #     #return HttpResponseRedirect('%d/editClient'% encrypted_password.id)
            # else:
            #      return HttpResponse("Bad Credentials. Please reload and Try again")

            if current_User.verify_password(pass1):
                #return redirect('accountcreated')
                if Client.objects.filter(user = current_User).exists():
                    return HttpResponseRedirect('%d/QuoteHistory'% current_User.id)
                else:
                    return HttpResponseRedirect('%d/editClient'% current_User.id)
            
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
    user_detail = get_object_or_404(User, pk=user_id)
    if Client.objects.filter(user = user_detail).exists():
        client_detail = get_object_or_404(Client, pk=user_detail)
        data = {'full_name':client_detail.name, 'address_1':client_detail.stAddress1, 'address_2':client_detail.stAddress2, 'state':client_detail.state, 'city':client_detail.city, 'zipcode':client_detail.zip }
    else:
        client_detail = Client(user=user_detail)
        data = {'full_name':"", 'address_1':"", 'address_2':"", 'state':"TX", 'city':"", 'zipcode':"" }
    
    if request.method == 'POST':
        form = clientForm(request.POST, initial = data)
        if form.is_valid():
            client_detail.name = form.cleaned_data['full_name']
            client_detail.stAddress1 = form.cleaned_data['address_1']
            client_detail.stAddress2 = form.cleaned_data['address_2']
            client_detail.city = form.cleaned_data['city']
            client_detail.state = form.cleaned_data['state']
            client_detail.zip = form.cleaned_data['zipcode']
            client_detail.save()
            return HttpResponseRedirect('/%d/QuoteHistory'% user_id) 

    else:
        form = clientForm(initial = data)

    context = {
        'form': form,
        'client_detail': client_detail,
    }

    return render(request, 'ClientForm.html', context)    

def fuelHist(request, user_id):
    #data = fuelQuote.objects.get(user=user_id)
    data = fuelQuote.objects.filter(user=user_id)
    context = {
         'data':data,
         'user_id': user_id,
    }
    return render(request, 'FuelQuoteHist.html', context)
    # context = {
    #     'user_id': user_id,
    # }
    # return render(request, 'FuelQuoteHist.html', context)




#Kevin's Views

# def index(request):
#     #return render(request, 'FuelQuoteForm.html')
#     return HttpResponseRedirect('quote/')

def fuelQuoteComplete(request, user_id):
    return HttpResponse('Fuel Quote Form Submitted Successfully')


def submitFuelQuote(request, user_id):
    user_detail = get_object_or_404(User, pk=user_id)
    client_detail = Client.objects.get(user=user_detail)
    fq = fuelQuote()
    fq.deliveryAddress = client_detail.stAddress1 + " " + client_detail.city + ", " + client_detail.state + " " + client_detail.zip
    form = fuelQuoteForm(request.POST)

    if request.method == 'POST':
        if 'get_quote' in request.POST:
            if form.is_valid():
                fq.user = user_detail
                fq.gallonsRequested = form.cleaned_data['gallons_requested']
                fq.deliveryDate = form.cleaned_data['delivery_date']
                fq.get_total_price()
    
        if 'submit_quote' in request.POST:
            if form.is_valid():
                fq.user = user_detail
                fq.gallonsRequested = form.cleaned_data['gallons_requested']
                fq.deliveryDate = form.cleaned_data['delivery_date']
                fq.get_total_price()
                fq.save()
                return HttpResponseRedirect('/%d/QuoteHistory'% user_id)
                #return HttpResponse('Form Saved')
                #return HttpResponseRedirect('complete/')
                #return HttpResponseRedirect('/%d/quote/created/'% user_id)
    else:   #if GET (or anything other method)
        form = fuelQuoteForm()

    context = {
        'form': form,
        'fq': fq,
        'client_detail': client_detail,
        'user_id': user_id,
    }

    return render(request, 'FuelQuoteForm.html', context)


#ajax attempts

# def created(request, user_id):
#     fq = fuelQuote()
#     fq.deliveryAddress = client_detail.stAddress1 + " " + client_detail.city + ", " + client_detail.state + " " + client_detail.zip

#     if request.method == 'POST':
#         if form.is_valid():
#             fq.gallonsRequested = request.POST['fq.gallonsRequested']
#             fq.deliveryAddress = request.POST['fq.deliveryAddress']
#             fq.get_total_price()
#             # fq.save()
#             return HttpResponse('create success')

#def testFunction(request, user_id):
    #return HttpResponse('Test Function Called')
    # user_detail = get_object_or_404(User, pk=user_id)
    # client_detail = Client.objects.get(user=user_detail)
    # fq = fuelQuote()
    # fq.deliveryAddress = client_detail.stAddress1 + " " + client_detail.city + ", " + client_detail.state + " " + client_detail.zip

    # if request.method == 'POST':
    #     form = fuelQuoteForm(request.POST)
    #     if form.is_valid():
    #         fq.user = user_detail
    #         fq.gallonsRequested = form.cleaned_data['gallons_requested']
    #         fq.deliveryDate = form.cleaned_data['delivery_date']
    #         fq.get_total_price()
    #         return HttpResponse('Return data to ajax call')

    
        
         
         