from django.db import models
from account.models import User
# Create your models here.


class Main_XR(models.Model):
    expense = models.IntegerField('Xarajat',default=0,null=True,blank=True)
    profit = models.FloatField("Daromat", default=0,null=True,blank=True)
    date = models.DateField("Vaqt", auto_now_add=True,)

    class Meta:
        ordering = ["-id"]
        verbose_name = "Asosiy X/R"

class Citygas_XR(models.Model):
    expense = models.FloatField('Xarajat',default=0,null=True,blank=True)
    profit = models.IntegerField("Daromat", default=0,null=True,blank=True)
    date = models.DateField("Vaqt", auto_now_add=True,)

    class Meta:
        ordering = ["-id"]
        verbose_name = "Xudud gaz X/R"


class Aksiz_XR(models.Model):
    expense = models.FloatField('Xarajat',default=0,null=True,blank=True)
    profit = models.IntegerField("Daromat", default=0,null=True,blank=True)
    date = models.DateField("Vaqt", auto_now_add=True,)

    class Meta:
        ordering = ["-id"]
        verbose_name = "Aksiz X/R"

class Election_XR(models.Model):
    expense = models.FloatField('Xarajat',default=0,null=True,blank=True)
    profit = models.IntegerField("Daromat", default=0,null=True,blank=True)
    date = models.DateField("Vaqt", auto_now_add=True,)

    class Meta:
        ordering = ["-id"]
        verbose_name = "Elektrosvet X/R"


class Credir_XR(models.Model):
    expense = models.IntegerField('Xarajat',default=0,null=True,blank=True)
    profit = models.IntegerField("Daromat", default=0,null=True,blank=True)
    date = models.DateField("Vaqt", auto_now_add=True,)

    class Meta:
        ordering = ["-id"]
        verbose_name = "Kredit X/R"


class Others_XR(models.Model):
    expense = models.IntegerField('Xarajat',default=0,null=True,blank=True)
    profit = models.IntegerField("Daromat", default=0,null=True,blank=True)
    date = models.DateField("Vaqt", auto_now_add=True,)

    class Meta:
        ordering = ["-id"]
        verbose_name = "Boshqa X/R"
        verbose_name_plural = "Boshqalar X/R"


class Addmaingas(models.Model):
    mian_gas = models.IntegerField("Gaz(kub)",default=0,null=True,blank=True)
    gas = models.IntegerField("Gaz(kub)",default=0,null=True,blank=True)
    buygasprice = models.IntegerField("Olinga narx",default=0,null=True,blank=True)
    salegasprice = models.IntegerField("Sotilgan narx",default=0,null=True,blank=True)
    cardprofid = models.IntegerField("Plastik sovda",default=0,null=True,blank=True)
    date = models.DateField("Vaqt", auto_now_add=True,)

    class Meta:
        ordering = ["-id"]
        verbose_name = "GAZ xisoblagich"
        verbose_name_plural = "Gaz xisoblagichlar X/R"