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
        obj.camp_id = request.POST.get("id")
        cid = obj.camp_id
        camp_list = Camp.objects.values_list('camp_id')
        camp_list = [i[0] for i in camp_list]
        if cid in camp_list:
            camp_data = Camp.objects.get(camp_id=cid)
            if camp_data.curr_capacity<=camp_data.total_capacity:
                camp_data.curr_capacity+=1
                obj.name = request.POST.get("name")
                obj.age = request.POST.get("age")
                obj.contact = request.POST.get("ph")
                obj.gender = request.POST.get("gen")
                camp_data.save(update_fields=['curr_capacity'])
                obj.save()
                return HttpResponseRedirect("Person")
            else:
                return render(request,'Person.html',{"error":"Capacity Full"})
        else:
            return render(request,'Person.html',{'error':"Invalid Camp ID"})
    return render(request,'Person.html',{"error":""})

def requirements(request):
    if request.POST:
        cid = request.POST.get("id")
        camp_list = Camp.objects.values_list('camp_id')
        camp_list = [i[0] for i in camp_list]
        if cid in camp_list:
            camp_data = Camp.objects.get(camp_id=cid)
    return render(request,'Requirements.html')

def test(request):
    data = Camp.objects.values_list('camp_id')
    data = [i[0] for i in data]
    return render(request,'Test.html',{"data":data})