from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth import authenticate,login,logout
def signup(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['pass1']
        confirm_password = request.POST['pass2']

        if password !=confirm_password:
            messages.warning(request, "Password is not matching")
            return render(request, "signup.html")
        
        try:
            User.objects.get(username = email)
            messages.info(request, "User Already Exists")
            return render(request, "signup.html")

        except User.DoesNotExist:
            pass

        user = User.objects.create_user(username=email, email=email, password=password)
        user.is_active=True
        user.save()
        messages.success(request, "Account created successfully. Please log in.")

        return redirect("home")
    return render(request,"signup.html")

def handle_login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method=="POST":
        username =request.POST['email']
        userpassword = request.POST['pass1']
        myuser = authenticate(username=username, password = userpassword)

        if myuser is not None:
            login(request, myuser)
            messages.success(request, "login successful")
            return redirect('/')
        
        else:
            messages.error(request,"invalid credentials")

            return redirect('login')
    return render(request,"login.html")



def handle_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully.")

    return redirect("home")

