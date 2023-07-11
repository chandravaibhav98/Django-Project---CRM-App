from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def login_user(request):
# Check to see if loggin in
    if request.method == 'POST':
        userName = request.POST['userName']
        passWord = request.POST['passWord']
        # Authenticate
        user = authenticate(request,username=userName,password=passWord)
        if user is not None:
            login(request,user)
            messages.success(request,'You are logged in')
            return redirect('home')
        else:
            messages.success(request,'Error; Please try Login again')
            
def home(request):
    # Check to see if loggin in
    login_user(request)
    return render(request, 'home.html', {})

def logout_user(request):
    logout(request)
    messages.success(request,"You've been logged out")
    return redirect('home')
