from django.contrib import admin
from django.urls import path
from wscubtech import views



urlpatterns = [
   
    path('calculator/',views.calculator,name='calculator'),
]
