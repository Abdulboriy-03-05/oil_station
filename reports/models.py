from django.db import models
from account.models import User
from django.urls import reverse
# Create your models here.


class Filial(models.Model):
    name = models.CharField("Filial nomi", max_length=50)
    slug = models.SlugField("*",unique=True)


    def get_url(self):
        return reverse("main:category_list", kwargs={"category_slug":self.slug,})
    
    def __str__(self):
        return "{}".format(self.name)
    
    

# class Aksiz_XR(models.Model):
#     expense = models.FloatField('Xarajat',default=0,null=True,blank=True)
#     profit = models.IntegerField("Daromat", default=0,null=True,blank=True)
#     date = models.DateField("Vaqt", auto_now_add=True,)

#     class Meta:
#         ordering = ["-id"]
#         verbose_name = "Aksiz X/R"

# class Election_XR(models.Model):
#     expense = models.FloatField('Xarajat',default=0,null=True,blank=True)
#     profit = models.IntegerField("Daromat", default=0,null=True,blank=True)
#     date = models.DateField("Vaqt", auto_now_add=True,)

#     class Meta:
#         ordering = ["-id"]
#         verbose_name = "Elektrosvet X/R"


# class Credir_XR(models.Model):
#     expense = models.IntegerField('Xarajat',default=0,null=True,blank=True)
#     profit = models.IntegerField("Daromat", default=0,null=True,blank=True)
#     date = models.DateField("Vaqt", auto_now_add=True,)

#     class Meta:
#         ordering = ["-id"]
#         verbose_name = "Kredit X/R"


class Saleprice(models.Model):
    saleprice = models.IntegerField('Gazdi olingan narxi',default=0,null=True,blank=True)
    date = models.DateField("Vaqt", auto_now_add=True,)

    class Meta:
        ordering = ["-id"]
        verbose_name = " Gazdi sotuv narxi"
        verbose_name_plural = "Gazdi sotuv narxi"
    def __str__(self):
        return f"{self.saleprice}"



class Buyprice(models.Model):
    buyprice = models.IntegerField('Gazdi sotilgan narxi',default=0,null=True,blank=True)
    date = models.DateField("Vaqt", auto_now_add=True,)

    class Meta:
        ordering = ["-id"]
        verbose_name = " Gazdi olingan narxi"
        verbose_name_plural = "Gazdi olingan narxi"
    
    def __str__(self):
        return f"{self.buyprice}"



class Losegas(models.Model):
    losegas = models.FloatField('1.4% Tabiy Yo\'qotish',default=1.4,null=True,blank=True)
    date = models.DateField("Vaqt", auto_now_add=True,)

    class Meta:
        ordering = ["-id"]
        verbose_name = " Gazdi 1.4% Yo'qotish"
        verbose_name_plural = " Gazdi 1.4% Yo'qotish"
    
    def __str__(self):
        return f"{self.losegas}"



class Addmaingas(models.Model):
    author = models.ForeignKey(User, verbose_name='User', on_delete=models.DO_NOTHING, default=None, null=True)
    category = models.ForeignKey(Filial,verbose_name="Filial",on_delete=models.DO_NOTHING, default=None, null=True,related_name="filials")
    last_gas = models.IntegerField("Sotib olingan gaz(kub)",null=True,blank=True)
    mian_gas = models.IntegerField("Gaz(kub)",null=True,blank=True)
    lose = models.FloatField("1.4% Yo'q",null=True,blank=True)
    remain = models.FloatField("Tani",null=True,blank=True)
    buygasprice = models.IntegerField("Olinga narx",null=True,blank=True)
    salegasprice = models.IntegerField("Sotilgan narx",null=True,blank=True)
    buy_sum = models.IntegerField("Umumiy(ol sum)",null=True,blank=True)
    sale_sum = models.IntegerField("Umumiy(sot sum)",null=True,blank=True)
    date = models.DateField("Vaqt", auto_now_add=True,)

    class Meta:
        ordering = ["-id"]
        verbose_name = "Asosiy gaz xisoblagich"
        verbose_name_plural = "Asosiy gaz xisoblagich X/R"
    
    def __str__(self):
        return f"{self.author}"
    



class Main_XR(models.Model):
    category = models.ForeignKey(Filial,verbose_name="Main_XR",on_delete=models.DO_NOTHING, default=None, null=True,related_name="filal_main_xr")
    main = models.IntegerField("Umumiy0",default=0,null=True,blank=True)
    date = models.DateField("Vaqt", auto_now_add=True,)

    class Meta:
        ordering = ["-id"]
        verbose_name = "Asosiy X/R"

class Main_XR_income(models.Model):
    category = models.ForeignKey(Filial,verbose_name="Main_XR_in_out", on_delete=models.DO_NOTHING, default=None,null=True,related_name="main_in_out")
    income = models.IntegerField("Main_income",default=0,null=True,blank=True)
    outcome = models.IntegerField("Main_outcome",default=0,null=True,blank=True)
    date = models.DateField("Vaqt", auto_now_add=True,)


    class Meta:
        ordering = ["-id"]
        verbose_name = "Asosiy IN OUT X/R"