from django.shortcuts import render

from django.utils.translation import get_language

def home(request):
    print(get_language())

    return render(request, 'home.html')
