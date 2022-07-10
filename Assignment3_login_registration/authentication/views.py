from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login


# Create your views here.
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

# def signout(request):
#     pass


