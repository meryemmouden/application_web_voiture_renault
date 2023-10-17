from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.

def home(request):
    return render(request,'users/home.html')

def register(request):
 if request.method=="POST":
     forms =UserRegisterForm(request.POST)
     if forms.is_valid():
       forms.save()
       return redirect('login')
 else:
     forms=UserRegisterForm()
 return render(request,'users/register.html',{'forms':forms})



@login_required(login_url='login')
def voiture(request):
    produits=product.objects.all()
    return render(request, 'users/voiture.html',{'produit':produits})
@login_required(login_url='login')
def acces(request):
    ac=accessoir.objects.all()
    return render(request, 'users/product.html',{'acs':ac})
@login_required(login_url='login')
def detail(request,pk):
    prod=product.objects.get(id=pk)
    return render(request,'users/detail.html',{'produit':prod})
@login_required(login_url='login')
def car(request,pk):
    ac=accessoir.objects.get(id=pk)
    return render(request,'users/car.html',{'produit':ac})



