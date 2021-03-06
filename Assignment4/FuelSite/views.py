from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Client
from .forms import clientForm

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login


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

        myuser = User.objects.create_user(username, email=None, password=pass1)

        myuser.save()

        messages.success(request, "Your Account has been successfully created.")

        return redirect('home')

    return render(request, "authentication/registration.html")


def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            return redirect('accountcreated')
            #user will log into the client profile page
            #return HttpResponse("you are successfully logged in")
        
        else:
            messages.error(request, "Bad Credentials")
            return redirect('home')
            #return HttpResponse("you are successfully logged in")
            #return HttpResonse("Bad Credentials, please reload the page and try again")

    return render(request, "authentication/login.html")

def accountcreated(request):
    return render(request, "authentication/successfullogin.html")




#Victoria's Views

def index(request):
    #return HttpResponse()
    return HttpResponseRedirect('registration/')
    #return HttpResponseRedirect(reverse('submitForm'), args)

def formComplete(request):
    return HttpResponse("Form Submitted, Thanks!")

def submitForm(request):
    #client_detail = get_object_or_404(Client, pk=user_id)
    client_detail = Client()
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
