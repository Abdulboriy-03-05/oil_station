from django.urls import path
from .import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    # path('main_reports', views.main_reports, name='main_reports'),
    path("<str:category_slug>/category/", views.category_list, name="category_list"),
    path("add_to_maingas",views.addmaingas,name='add_to_maingas'),
    path("add_to_incoms",views.addincome,name='add_to_incomes'),
    path("station_add_gas",views.station_add_gas,name='station_add_gas'),
    path("add_card_incomes",views.add_card_income,name='add_card_income'),
    # path("all_sale_gas",views.all_sale_gas,name='all_sale_gas'),
]