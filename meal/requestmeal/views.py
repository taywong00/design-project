from django.shortcuts import render
from django.http import HttpResponse
#from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm


def index(request):
    return render(request, 'requestmeal/home.html')

def about(request):
    return render(request, 'requestmeal/about.html')

def register(request):
    if request.method == 'POST':  
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            #save user info
    else:
        form = RegistrationForm()
    return render(request, 'requestmeal/register.html', {'form': form})

def menu(request):
    return render(request, 'requestmeal/menu.html')