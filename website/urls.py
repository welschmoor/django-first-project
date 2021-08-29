from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('add/', views.add, name="add"), 
    path('subtract/', views.subtract, name="subtract"), 
    path('multiply/', views.multiply, name="multiply"), 
    path('divide/', views.divide, name="divide"), 
]
