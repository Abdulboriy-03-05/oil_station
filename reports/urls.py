from django.urls import path
from .import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path("<str:category_slug>/category/", views.category_list, name="category_list"),
    path("detail/<int:p_id>/", views.postDetail, name='detail'),
    path("add_to_maingas/",views.addmaingas,name='add_to_maingas'),
    path("add_to_maingas_yestarday/",views.addmaingasyes,name='add_to_maingas_yestarday'),
    path("add_to_incoms/",views.addincome,name='add_to_incomes'),
    path("pay_credit/",views.pay_credit,name='pay_credit'),
    path("borrow_money/",views.get_money,name='borrow_money'),
    path("additional_money/",views.additionalmoney,name='additional_money'),
    path("station_add_gas/",views.station_add_gas,name='station_add_gas'),
    path("add_card_incomes/",views.add_card_income,name='add_card_income'),
    path("all_sale_gas_nasirullo/",views.all_sale_gas_nas,name='all_sale_gas_nasirullo'),
    path("all_sale_gas_sanoat/",views.all_sale_gas_san,name='all_sale_gas_sanoat'),
    path("all_sale_gas_parfum/",views.all_sale_gas_par,name='all_sale_gas_parfum'),
    path("nasirullo_outcome/",views.nasirullo_outcome,name='nasirullo_outcome'),
    path("sanoat_outcome/",views.sanoat_outcome,name='sanoat_outcome'),
    path("parfum_outcome/",views.parfum_outcome,name='parfum_outcome'),
    path("nasirullo_company/",views.nasirullo_company,name='nasirullo_company'),
    path("parfum_company/",views.parfum_company,name='parfum_company'),
    path("nasirullo_gas_raports/",views.nasgasraports,name='nasirullo_gas_raports'),
    path("sanoat_gas_raports/",views.sanoatgasraports,name='sanoat_gas_raports'),
    path("parfum_gas_raports/",views.parfumgasraports,name='parfum_gas_raports'),
    path("main_reports_nasirullo/",views.main_reports_nas,name='main_reports_nasirullo'),
    path("main_reports_sanoat/",views.main_reports_san,name='main_reports_sanoat'),
    path("main_reports_parfum/",views.main_reports_par,name='main_reports_parfum'),
    path("nasirullo_aksiz_raports/",views.nasirulloaksizraports,name='nasirullo_aksiz_raports'),
    path("sanoat_aksiz_raports/",views.sanoataksizraports,name='sanoat_aksiz_raports'),
    path("parfum_aksiz_raports/",views.parfumaksizraports,name='parfum_aksiz_raports'),
    path("nasirullo_elector_raports/",views.nasirulloelectorraports,name='nasirullo_elector_raports'),
    path("sanoat_elector_raports/",views.sanoatelectorraports,name='sanoat_elector_raports'),
    path("parfum_elector_raports/",views.parfumelelectorraports,name='parfum_elector_raports'),
    
]