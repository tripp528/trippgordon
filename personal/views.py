from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'personal/about.html')

def about(request):
    return render(request, 'personal/about.html')

def rest(request):
    return render(request, 'personal/rest.html')

def awards(request):
    return render(request, 'personal/awards.html')

def looping(request):
    return render(request, 'personal/looping.html', {'content':['awards1','awards2']})
