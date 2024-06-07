from django.urls import path
from .import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path("<str:category_slug>/category/", views.category_list, name="category_list"),
    path("add_to_maingas",views.addmaingas,name='add_to_maingas'),
]