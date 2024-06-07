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
    list_diplay = ["main"]

@admin.register(Xududgaz_XR)
class Xududgaz_XRAdmin(admin.ModelAdmin):
    list_diplay = ["bill"]

@admin.register(Aksiz_XR)
class Aksiz_XRAdmin(admin.ModelAdmin):
    list_diplay = ["bill"]


@admin.register(Main_XR_income)
class Main_XR_incomeAdmin(admin.ModelAdmin):
    list_diplay = ["income","outcome"]

@admin.register(Xudud_XR_income)
class Xudud_XR_incomeAdmin(admin.ModelAdmin):
    list_diplay = ["income","outcome"]

@admin.register(Aksiz)
class Aksiz_XRAdmin(admin.ModelAdmin):
    list_diplay = ['aksiz']

@admin.register(Addmaingas)
class AddmaingasAdmin(admin.ModelAdmin):
    list_diplay = ['author','filial']