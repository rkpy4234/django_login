from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
    context = {}
    return render(request, "authApp/home.html",context)

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('../users/')
        else:
            return render(request, 'authApp/login.html', {'error': 'Invalid username or password'})

    return render(request, "authApp/login.html")

#for register page
def register_page(request):
    return render(request, "authApp/register.html")

#for users page
def users_page(request):
    return render(request, "authApp/users.html")

