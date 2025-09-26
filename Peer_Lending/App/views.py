from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import CustomUserCreationForm


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            messages.success(request, "Account created successfully!")
            return redirect("home")
        else:
            messages.error(request, "Please correct the errors below.")
            print(form.errors)  # Check the console for validation errors
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

def home(request):
    return render(request, "home.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "registration/login.html")

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")
    else:
        return redirect("home") 