from django.shortcuts import render, redirect
from .models import Restaurant

# Create your views here.
def index(request):
    restaurant = Restaurant.objects.all()
    context = {
        'restaurants' : restaurant
    }
    return render(request, "restaurants/index.html", context)

def new(request):
    return render(request, "restaurants/create.html")

def create(request):
    name = request.POST.get("name")
    description = request.POST.get("description")
    phone = request.POST.get("phone")
    address = request.POST.get("address")

    todo = Restaurant(name = name, address = address, description = description, phone_number = phone)
    todo.save()
    return redirect("restaurants:index")