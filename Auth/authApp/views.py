from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    return render(request, "authApp/home.html",context)

def login_page(request):
    return render(request, "authApp/login.html")

