from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")
def login(request):
    return render(request, "login.html")
def signup(request):
    return render(request, "signup.html")
def cart(request):
    return render(request, "cart.html")
def payment(request):
    return render(request, "payment.html")
def gromart(request):
    return render(request, "grocery mart.html")
def pesticides(request):
    return render(request, "pesticides.html")
def fruits(request):
    return render(request, "fruits.html")
def vegetables(request):
    return render(request, "vegetabels.html")
def grains(request):
    return render(request, "grains.html")
def Account(request):
    return render(request, "Account.html")
def Order(request):
    return render(request, "Order.html")
