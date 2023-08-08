from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('Camp',views.camp),
    path('Person',views.person),
    path('Requirements',views.requirements),
    path('test',views.test),
]