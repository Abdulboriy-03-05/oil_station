from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Filial)
class FilialAdmin(admin.ModelAdmin):
    list_diplay = ['name','slug']


@admin.register(Addmaingas)
class AddmaingasAdmin(admin.ModelAdmin):
    list_diplay = ['author','filial']



@admin.register(Saleprice)
class SalepriceAdmin(admin.ModelAdmin):
    list_diplay = ['saleprice','date']

@admin.register(Buyprice)
class BuypriceAdmin(admin.ModelAdmin):
    list_diplay = ['saleprice','date']

@admin.register(Nasrullo_lose)
class LosegasAdmin(admin.ModelAdmin):
    list_diplay = ['losegas','date']


@admin.register(Sanoat_lose)
class LosegasAdmin(admin.ModelAdmin):
    list_diplay = ['losegas','date']


@admin.register(Parfum_lose)
class LosegasAdmin(admin.ModelAdmin):
    list_diplay = ['losegas','date']

@admin.register(Aksiz)
class Aksiz_XRAdmin(admin.ModelAdmin):
    list_diplay = ['aksiz']

@admin.register(Elector)
class ElectorAdmin(admin.ModelAdmin):
    list_diplay = ['aksiz']

@admin.register(Send)
class SendAdmin(admin.ModelAdmin):
    list_diplay = ['send_tax']



@admin.register(Main_XR)
class Main_XRAdmin(admin.ModelAdmin):
    list_diplay = ["main"]

@admin.register(Xududgaz_XR)
class Xududgaz_XRAdmin(admin.ModelAdmin):
    list_diplay = ["bill"]

@admin.register(Aksiz_XR)
class Aksiz_XRAdmin(admin.ModelAdmin):
    list_diplay = ["bill"]

@admin.register(Elector_XR)
class Elector_XRAdmin(admin.ModelAdmin):
    list_diplay = ["bill"]


@admin.register(Company_XR)
class Company_XRAdmin(admin.ModelAdmin):
    list_diplay = ["bill"]

@admin.register(Credit)
class CreditAdmin(admin.ModelAdmin):
    list_diplay = ["bill"]




@admin.register(Main_XR_income)
class Main_XR_incomeAdmin(admin.ModelAdmin):
    list_diplay = ["income"]

@admin.register(Main_XR_outcome)
class Main_XR_outcomeAdmin(admin.ModelAdmin):
    list_diplay = ["outcome"]

@admin.register(Xudud_XR_income)
class Xudud_XR_incomeAdmin(admin.ModelAdmin):
    list_diplay = ["income"]

@admin.register(Xudud_XR_outcome)
class Xudud_XR_outcomeAdmin(admin.ModelAdmin):
    list_diplay = ["outcome"]


@admin.register(Aksiz_XR_income)
class Aksiz_XR_incomeAdmin(admin.ModelAdmin):
    list_diplay = ["income"]

@admin.register(Aksiz_XR_outcome)
class Aksiz_XR_outcomeAdmin(admin.ModelAdmin):
    list_diplay = ["outcome"]


@admin.register(Elector_XR_income)
class Aksiz_XR_incomeAdmin(admin.ModelAdmin):
    list_diplay = ["income"]

@admin.register(Elector_XR_outcome)
class Elector_XR_outcomeAdmin(admin.ModelAdmin):
    list_diplay = ["outcome"]



@admin.register(Company_XR_income)
class Company_XR_incomeAdmin(admin.ModelAdmin):
    list_diplay = ["income"]

@admin.register(Others)
class Others_incomeAdmin(admin.ModelAdmin):
    list_diplay = ["income"]

@admin.register(Credit_income)
class Credit_incomeAdmin(admin.ModelAdmin):
    list_diplay = ["income"]



@admin.register(Incomes)
class IncomeAdmin(admin.ModelAdmin):
    list_diplay = ["name","slug"]


@admin.register(Income_XRS)
class Income_XRSAdmin(admin.ModelAdmin):
    list_diplay = ["income","sum"]


@admin.register(Manag_add_gas)
class Manag_add_gasAdmin(admin.ModelAdmin):
    list_diplay = ["category"]


@admin.register(Manag_totals)
class Manag_totalsAdmin(admin.ModelAdmin):
    list_diplay = ["category"]