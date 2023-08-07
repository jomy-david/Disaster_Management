from django.shortcuts import render
from .models import Person,Camp
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    return render(request,'Home.html')

def camp(request):
    obj = Camp.objects.all()
    return render(request,'Camp.html',{"obj":obj})

def person(request):
    if request.POST:
        obj = Person()
        obj.name = request.POST.get("name")
        obj.age = request.POST.get("age")
        obj.camp_id = request.POST.get("id")
        obj.contact = request.POST.get("ph")
        obj.gender = request.POST.get("gen")
        obj.save()
        return HttpResponseRedirect("Person")
    return render(request,'Person.html')

def requirements(request):
    return render(request,'Requirements.html')