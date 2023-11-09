from django.shortcuts import render
from .models import Person,Camp
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    return render(request,'Home.html')

def camp(request):
    obj = Camp.objects.all()
    obj_per = Person.objects.all()
    camp_list = Camp.objects.values_list('camp_id')
    camp_list = [i[0] for i in camp_list]
    per_camp_list = Person.objects.values_list('camp_id')
    per_camp_list = [i[0] for i in per_camp_list]
    for i in camp_list:
        obj_camp = Camp.objects.get(camp_id=i)
        obj_camp.curr_capacity=per_camp_list.count(i)
        obj_camp.save(update_fields=['curr_capacity'])
    return render(request,'Camp.html',{"obj":obj,"data_per":obj_per})

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
                obj.name = request.POST.get("name")
                if obj.name.isspace():
                    return render(request,'Person.html',{"error":"*Name cannot be empty"})
                obj.age = request.POST.get("age")
                obj.contact = request.POST.get("ph")
                obj.gender = request.POST.get("gen")
                obj.save()
                return HttpResponseRedirect("Person")
            else:
                return render(request,'Person.html',{"error":"*Capacity Full"})
        else:
            return render(request,'Person.html',{'error':"*Invalid Camp ID"})
    return render(request,'Person.html',{"error":""})

def requirements(request):
    if request.POST:
        cid = request.POST.get("id")
        camp_list = Camp.objects.values_list('camp_id')
        camp_list = [i[0] for i in camp_list]
        if cid in camp_list:
            camp_data = Camp.objects.get(camp_id=cid)
            ration = request.POST.get("things")
            qty = int(request.POST.get("qty"))
            if ration == "towels":
                camp_data.rat_towel+=qty
            else:
                camp_data.rat_soap+=qty
            camp_data.save(update_fields=['rat_towel','rat_soap'])
        else:
            return render(request,'Requirements.html',{'error':"Invalid Camp ID"})
    return render(request,'Requirements.html',{"error":""})

def test(request):
    data = Camp.objects.values_list('camp_id')
    data = [i[0] for i in data]
    name = "  "
    d = name.isspace()
    return render(request,'Test.html',{"data":d})