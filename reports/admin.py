from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Main_XR)
class Main_XRAdmin(admin.ModelAdmin):
    list_diplay = ['expense','profit']

@admin.register(Citygas_XR)
class Citygas_XRAdmin(admin.ModelAdmin):
    list_diplay = ['expense','profit']

@admin.register(Aksiz_XR)
class Aksiz_XRAdmin(admin.ModelAdmin):
    list_diplay = ['expense','profit']

@admin.register(Election_XR)
class Election_XRAdmin(admin.ModelAdmin):
    list_diplay = ['expense','profit']

@admin.register(Credir_XR)
class Credir_XRAdmin(admin.ModelAdmin):
    list_diplay = ['expense','profit']

@admin.register(Others_XR)
class Others_XRAdmin(admin.ModelAdmin):
    list_diplay = ['expense','profit']

@admin.register(Addmaingas)
class AddmaingasAdmin(admin.ModelAdmin):
    list_diplay = ['expense','profit']