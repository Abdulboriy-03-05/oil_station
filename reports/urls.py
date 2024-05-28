from django.urls import path
from .import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path("add_to_maingas",views.addmaingas,name='add_to_maingas'),
]