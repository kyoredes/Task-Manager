from django.shortcuts import render
from django.views import View
from django.utils import translation

def home(request):
    return render(request, 'home.html')
