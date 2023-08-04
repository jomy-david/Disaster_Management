from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'Home.html')

def camp(request):
    return render(request,'Camp.html')

def person(request):
    return render(request,'Person.html')

def requirements(request):
    return render(request,'Requirements.html')