from django.shortcuts import render,redirect
from travelapp.models import Contact

# Create your views here.
def home(request):
    return render(request, 'index.html')


def service(request):
    return render(request, 'service.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')