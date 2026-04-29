from django.contrib import admin
from django.urls import path
from wscubtech import views



urlpatterns = [
    path('',views.Home),
    path('admin/', admin.site.urls),
    path('aboutUs/',views.aboutUs,name='aboutUs'),
    path('calculator/',views.calculator,name='calculator'),
]
