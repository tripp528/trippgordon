from django.shortcuts import render
from django.http import HttpResponse

def default(request):
    return render(request, 'personal/about.html')

def about(request):
    return render(request, 'personal/about.html')

def portfolio(request):
    return render(request, 'personal/portfolio.html')

def template(request):
    return render(request, 'personal/template.html')
