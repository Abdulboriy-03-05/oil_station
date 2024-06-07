from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Filial)
class FilialAdmin(admin.ModelAdmin):
    list_diplay = ['name','slug']

@admin.register(Saleprice)
class SalepriceAdmin(admin.ModelAdmin):
    list_diplay = ['saleprice','date']

@admin.register(Buyprice)
class BuypriceAdmin(admin.ModelAdmin):
    list_diplay = ['saleprice','date']

@admin.register(Losegas)
class LosegasAdmin(admin.ModelAdmin):
    list_diplay = ['losegas','date']

@admin.register(Main_XR)
class Main_XRAdmin(admin.ModelAdmin):
    list_diplay = ["income","outcome"]

@admin.register(Main_XR_income)
class Main_XR_incomeAdmin(admin.ModelAdmin):
    list_diplay = ["income","outcome"]

# @admin.register(Others_XR)
# class Others_XRAdmin(admin.ModelAdmin):
#     list_diplay = ['expense','profit']

@admin.register(Addmaingas)
class AddmaingasAdmin(admin.ModelAdmin):
    list_diplay = ['author','filial']