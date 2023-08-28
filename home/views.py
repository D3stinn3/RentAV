from django.shortcuts import render, redirect
from home.forms import homeUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def homePage(request):
    context = {}
    return render(request, 'hometemp/home.html', context)

def landingPage(request):
    context = {}
    return render(request, 'hometemp/base.html', context)

def signupPage(request):
    
    if request.method == "POST":
        form = homeUserForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Registration Successful")
            return redirect('login')
        else:
            for msg in form._errors.values():
                errmsg = f"{msg[0]}"
                messages.error(request, errmsg)
                
    form = homeUserForm()
    context = {'form': form}
    return render(request, 'hometemp/signin.html', context)

def loginPage(request):
    
    if request.method == "POST":
        user = authenticate(
            email = request.POST['email'],
            password = request.POST['password']
        )
        
        if user is not None and user.is_client:
            login(request, user)
            messages.success(request, "Login Successful")
            return redirect('client')
        
        elif user is not None and user.is_dealer:
            login(request, user)
            messages.success(request, "Login Successful")
            return redirect('dealer')
        
    context = {}
    return render(request, 'hometemp/login.html', context)

def dealerPage(request):
    user = request.user
    context = {'user': user}
    return render(request, 'hometemp/dealer.html', context)

def clientPage(request):
    user = request.user
    context = {'user': user}
    return render(request, 'hometemp/client.html', context)

def thePage(request):
    user = request.user
    context = {'user': user}
    return render(request, 'hometemp/page.html', context)

def logoutPage(request):
    logout(request)
    return redirect('home')          