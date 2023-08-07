from django.contrib import admin
from .models import Person,Camp

# Register your models here.

class adminPerson(admin.ModelAdmin):
    list_display=[
        'name','age','camp_id','contact','gender'
    ]
class adminCamp(admin.ModelAdmin):
    list_display=[
        'camp_id','camp_name','camp_add','camp_district','camp_state','camp_man','man_id','camp_img','man_contact'
    ]
admin.site.register(Person,adminPerson)
admin.site.register(Camp,adminCamp)
