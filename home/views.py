from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def dashboard(request):

    # Page from the theme 
    return render(request, 'pages/index.html')

def virtual(request):

    # Page from the theme 
    return render(request, 'pages/virtual-reality.html')
def profile(request):

    # Page from the theme 
    return render(request, 'pages/profile.html')
def bill(request):

    # Page from the theme 
    return render(request, 'pages/billing.html')
def table(request):

    # Page from the theme 
    return render(request, 'pages/tables.html')
def rtl(request):

    # Page from the theme 
    return render(request, 'pages/rtl.html')
