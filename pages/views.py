from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'pages/landing_page.html')

def cv(request):
    return render(request, 'pages/resume.html')