from django.contrib import admin
from .models import Person

# Register your models here.

class adminPerson(admin.ModelAdmin):
    list_display=[
        'name','age','camp_id','contact','gender'
    ]

admin.site.register(Person,adminPerson)