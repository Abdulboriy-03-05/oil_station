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
    
    

class Saleprice(models.Model):
    saleprice = models.IntegerField('Gazni olingan narxi',default=0,null=True,blank=True)
    date = models.DateField("Vaqt", auto_now_add=True,)

    class Meta:
        ordering = ["-id"]
        verbose_name = " Gazni sotuv narxi"
        verbose_name_plural = "Gazni sotuv narxi"
    def __str__(self):
        return f"{self.saleprice}"



class Buyprice(models.Model):
    buyprice = models.IntegerField('Gazdi sotilgan narxi',default=0,null=True,blank=True)
    date = models.DateField("Vaqt", auto_now_add=True,)

    class Meta:
        ordering = ["-id"]
        verbose_name = " Gazni olingan narxi"
        verbose_name_plural = "Gazni olingan narxi"
    
    def __str__(self):
        return f"{self.buyprice}"



class Nasrullo_lose(models.Model):
    losegas = models.FloatField('1.4% Tabiy Yo\'qotish',default=1.4,null=True,blank=True)
    date = models.DateField("Vaqt", auto_now_add=True,)

    class Meta:
        ordering = ["-id"]
        verbose_name = "Nasrullo gazni yo'qotishi"
        verbose_name_plural = " Nasrullo gazni yo'qotishi"
    
    def __str__(self):
        return f"{self.losegas}"
    

class Sanoat_lose(models.Model):
    losegas = models.FloatField('1.4% Tabiy Yo\'qotish',default=1.4,null=True,blank=True)
    date = models.DateField("Vaqt", auto_now_add=True,)

    class Meta:
        ordering = ["-id"]
        verbose_name = " Sanoat gazni yo'qotishi"
        verbose_name_plural = " Sanoat gazni yo'qotishi"
    
    def __str__(self):
        return f"{self.losegas}"


class Parfum_lose(models.Model):
    losegas = models.FloatField('1.4% Tabiy Yo\'qotish',default=1.4,null=True,blank=True)
    date = models.DateField("Vaqt", auto_now_add=True,)

    class Meta:
        ordering = ["-id"]
        verbose_name = " Parfum gazni yo'qotishi"
        verbose_name_plural = " Parfum gazni yo'qotishi"
    
    def __str__(self):
        return f"{self.losegas}"


class Aksiz(models.Model):
    aksiz = models.IntegerField('Aksiz solig\'',default=680,null=True,blank=True)
    date = models.DateField("Vaqt", auto_now_add=True,)

    class Meta:
        ordering = ["-id"]
        verbose_name = " Aksiz solig'"
        verbose_name_plural = " Aksiz solig'"
    
    def __str__(self):
        return f"{self.aksiz}"


class Elector(models.Model):
    elector = models.IntegerField('Elektor solig\'',default=0,null=True,blank=True)
    date = models.DateField("Vaqt", auto_now_add=True,)

    class Meta:
        ordering = ["-id"]
        verbose_name = " Elektor solig'"
        verbose_name_plural = " Elektor solig'"
    
    def __str__(self):
        return f"{self.elector}"


class Send(models.Model):
    send_tax = models.FloatField("Pul o'tkazish %'",default=0,null=True,blank=True)
    date = models.DateField("Vaqt", auto_now_add=True,)

    class Meta:
        ordering = ["-id"]
        verbose_name = "Pul o'tkazish %"
        verbose_name_plural = "Pul o'tkazish %"
    
    def __str__(self):
        return f"{self.send_tax}"



class Addmaingas(models.Model):
    author = models.ForeignKey(User, verbose_name='User', on_delete=models.DO_NOTHING, default=None, null=True)
    category = models.ForeignKey(Filial,verbose_name="Filial",on_delete=models.DO_NOTHING, default=None, null=True,related_name="filials")
    last_gas = models.IntegerField("Sotib olingan gaz(kub)", default=0,null=True,blank=True)
    lose_gas = models.FloatField("Yo'qotilgan gaz", default=0,null=True,blank=True)
    remain_gas = models.PositiveIntegerField("Qoldiq", default=0,null=True,blank=True)
    buygasprice = models.IntegerField("Gazning olinga narxi", default=0,null=True,blank=True)
    sale_price = models.PositiveIntegerField('Gazning sotish narxi', default=0,null=True,blank=True)
    aksiz = models.IntegerField("Aksiz solig' narxi", default=0,null=True,blank=True)
    elector = models.IntegerField("Elektor solig' narxi", default=0,null=True,blank=True)
    buy_sum = models.IntegerField("Umumiy(ol sum)",default=0,null=True,blank=True)
    aksiz_sum = models.IntegerField("Aksiz olingan narxi",default=0, null=True,blank=True)
    elec_sum = models.IntegerField("Elekctorga olingan narxi",default=0, null=True,blank=True)
    chec = models.PositiveIntegerField('Naqt',null=True, default=0,blank=True)
    card = models.PositiveIntegerField('Plastik karta',null=True, default=0,blank=True)
    card_uz = models.PositiveIntegerField('Uzcard karta',null=True, default=0,blank=True)
    card_humo = models.PositiveIntegerField('Humo karta',null=True, default=0,blank=True)
    company = models.PositiveIntegerField('Tashkilotlar',null=True, default=0,blank=True)
    sum_half = models.PositiveIntegerField('Daromat',default=0,null=True,blank=True)
    have_money = models.PositiveIntegerField("Tushgan pul", default=0,null=True,blank=True)
    no_money = models.PositiveIntegerField("Qolgan pul", default=0,null=True,blank=True)
    total_sum = models.PositiveIntegerField('Umumiy sovda',default=0,null=True,blank=True)
    profit = models.PositiveIntegerField("Foyda",default=0,null=True,blank=True)
    naqt = models.BooleanField("Naqt",default=False,)
    uzcard = models.BooleanField("Uzcard", default=False)
    humo = models.BooleanField("Humo", default=False)
    date = models.DateField("Vaqt",)

    class Meta:
        ordering = ["-id"]
        verbose_name = "Asosiy gaz xisoblagich"
        verbose_name_plural = "Asosiy gaz xisoblagich"
    
    def __str__(self):
        return f"{self.category, self.date}"
    


class Borrow_money(models.Model):
    bring_money = models.ForeignKey(Filial, verbose_name="Qayerdan*",on_delete=models.DO_NOTHING, default=None, null=True,related_name="bring_money") 
    get_money = models.ForeignKey(Filial, verbose_name="Qayerga*",on_delete=models.DO_NOTHING, default=None, null=True,related_name="get_money") 
    bill = models.PositiveIntegerField("Summa*", default=0, null=True, blank=True)
    date = models.DateField("Vaqt",)

    class Meta:
        verbose_name = "O'zaro otkazma"
        verbose_name_plural = "O'zaro otkazmalar"
    
    def __str__(self):
        return f"{self.date, self.bring_money}"



class Main_XR(models.Model):
    category = models.ForeignKey(Filial,verbose_name="Main_XR",on_delete=models.DO_NOTHING, default=None, null=True,related_name="filal_main_xr")
    bill = models.IntegerField("Umumiy",default=0,null=True,blank=True)
    date = models.DateField("Vaqt",)

    class Meta:
        verbose_name = "Asosiy X/R"
        verbose_name_plural = "Asosiy X/R"
    
    def __str__(self):
        return f"{self.category,self.date}"

class Main_XR_income(models.Model):
    category = models.ForeignKey(Filial,verbose_name="Qayerga*", on_delete=models.DO_NOTHING, default=None,null=True,related_name="main_income")
    income = models.IntegerField("Summa*",default=0,null=True,blank=True)
    description = models.TextField("Qayerdan*", max_length=50)
    date = models.DateField("Vaqt", auto_now_add=True,)
 
    class Meta:
        ordering = ["-id"]
        verbose_name = "Asosiy Income X/R"
    
    def __str__(self):
        return f"{self.category}"




class Main_XR_outcome(models.Model):
    category = models.ForeignKey(Filial,verbose_name="Main_XR_outcome", on_delete=models.DO_NOTHING, default=None,null=True,related_name="main_outcome")
    outcome = models.IntegerField("Main_outcome",default=0,null=True,blank=True)
    description = models.TextField("Izoh")
    date = models.DateField("Vaqt",)

    class Meta:
        ordering = ["-id"]
        verbose_name = "Asosiy Outcome X/R"
    
    def __str__(self):
        return f"{self.category}"
    

class Xududgaz_XR(models.Model):
    category = models.ForeignKey(Filial,verbose_name="Xududgaz", on_delete=models.DO_NOTHING, default=None,null=True,related_name="xududgaz")
    bill = models.IntegerField("Xududgaz xisob", default=0,null=True,blank=True)
    date = models.DateField("Vaqt")

    class Meta:
        verbose_name = "Xududgaz xisob"

    def __str__(self):
        return f"{self.category}"
    


class Xudud_XR_income(models.Model):
    category = models.ForeignKey(Filial,verbose_name="Xudud_income", on_delete=models.DO_NOTHING, default=None,null=True,related_name="xudud_income")
    income = models.IntegerField("Xudud income",default=0,null=True,blank=True)
    date = models.DateField("Vaqt", auto_now_add=True,)

    class Meta:
        ordering = ["-id"]
        verbose_name = "Xudud gaz Income X/R"
    
    def __str__(self):
        return f"{self.category}"




class Xudud_XR_outcome(models.Model):
    category = models.ForeignKey(Filial,verbose_name="Xudud_outcome", on_delete=models.DO_NOTHING, default=None,null=True,related_name="xudud_outcome")
    outcome = models.IntegerField("Xudud_outcome",default=0,null=True,blank=True)
    date = models.DateField("Vaqt", auto_now_add=True,)


    class Meta:
        ordering = ["-id"]
        verbose_name = "Xudud gaz Outcome X/R"
    
    def __str__(self):
        return f"{self.category}"
    


class Aksiz_XR(models.Model):
    category = models.ForeignKey(Filial,verbose_name="Aksiz", on_delete=models.DO_NOTHING, default=None,null=True,related_name="aksiz")
    bill = models.IntegerField("Aksiz xisob", default=0,null=True,blank=True)
    date = models.DateField("Vaqt")


    class Meta:
        verbose_name = "Aksiz xisob"

    def __str__(self):
        return f"{self.category}"
    


class Aksiz_XR_income(models.Model):
    category = models.ForeignKey(Filial,verbose_name="Aksiz_income", on_delete=models.DO_NOTHING, default=None,null=True,related_name="aksiz_income")
    income = models.IntegerField("Aksiz income",default=0,null=True,blank=True)
    date = models.DateField("Vaqt", auto_now_add=True,)

    class Meta:
        ordering = ["-id"]
        verbose_name = "Aksiz Income X/R"
    
    def __str__(self):
        return f"{self.category}"



class Aksiz_XR_outcome(models.Model):
    category = models.ForeignKey(Filial,verbose_name="Aksiz_outcome", on_delete=models.DO_NOTHING, default=None,null=True,related_name="aksiz_outcome")
    outcome = models.IntegerField("Aksiz outcome",default=0,null=True,blank=True)
    date = models.DateField("Vaqt", auto_now_add=True,)


    class Meta:
        ordering = ["-id"]
        verbose_name = "Aksiz Outcome X/R"
    
    def __str__(self):
        return f"{self.category}"
    


class Elector_XR(models.Model):
    category = models.ForeignKey(Filial,verbose_name="Elektrosvet", on_delete=models.DO_NOTHING, default=None,null=True,related_name="elctor")
    bill = models.IntegerField("Elektro svet xisob", default=0, null=True,blank=True)
    date = models.DateField("Vaqt")

    class Meta:
        verbose_name = "Elektro svet"
        verbose_name_plural = "Elektro svet"

    def __str__(self):
        return f"{self.category}"



class Elector_XR_income(models.Model):
    category = models.ForeignKey(Filial,verbose_name="Elektor_income", on_delete=models.DO_NOTHING, default=None,null=True,related_name="elctor_income")
    income = models.IntegerField("Elektor income",default=0,null=True,blank=True)
    date = models.DateField("Vaqt")


    class Meta:
        ordering = ["-id"]
        verbose_name = "Elektor svet income X/R"
        verbose_name_plural = "Elektor svet income X/R"
    
    def __str__(self):
        return f"{self.category}"
    


class Elector_XR_outcome(models.Model):
    category = models.ForeignKey(Filial,verbose_name="Elektor_outcome", on_delete=models.DO_NOTHING, default=None,null=True,related_name="elctor_outcome")
    outcome = models.IntegerField("Elektor outcome",default=0,null=True,blank=True)
    date = models.DateField("Vaqt", auto_now_add=True,)


    class Meta:
        ordering = ["-id"]
        verbose_name = "Elektor svet outcomeX/R"
        verbose_name_plural = "Elektor svet outcome X/R"
    
    def __str__(self):
        return f"{self.category}"



class Company_XR(models.Model):
    category = models.ForeignKey(Filial,verbose_name="Tashkilot", on_delete=models.DO_NOTHING, default=None,null=True,related_name="tashkilot")
    bill = models.IntegerField("Tashkilot xisob", default=0,null=True,blank=True)
    date = models.DateField("Vaqt")


    class Meta:
        verbose_name = "Tashkilot"
        verbose_name_plural = "Tashkilotlar"

    def __str__(self):
        return f"{self.category}"
    


class Company_XR_income(models.Model):
    category = models.ForeignKey(Filial,verbose_name="Tashkilot_income", on_delete=models.DO_NOTHING, default=None,null=True,related_name="companies_income")
    income = models.IntegerField("Tashkilot income",default=0,null=True,blank=True)
    date = models.DateField("Vaqt",)


    class Meta:
        ordering = ["-id"]
        verbose_name = "Tashkilotlar Income X/R"
    
    def __str__(self):
        return f"{self.category}"
    



class Debts(models.Model):
    category = models.ForeignKey(Filial,verbose_name="Qarzlar berilgan", on_delete=models.DO_NOTHING, default=None,null=True,related_name="qarzlar_bergan")
    debt = models.IntegerField("Qarzlar",default=0,null=True,blank=True)
    date = models.DateField("Vaqt",)

    class Meta:
        ordering = ["-id"]
        verbose_name = "Qarzlar bergan"
    
    def __str__(self):
        return f"{self.category}"



class Credit(models.Model):
    category = models.ForeignKey(Filial,verbose_name='Kredit', on_delete=models.DO_NOTHING,default=None, null=True, related_name='kredit')
    bill = models.IntegerField('Kredit to\'lov', default=0,null=True,blank=True)
    date = models.DateField('Vaqt')

    class Meta:
        verbose_name = 'Kredit to\'lov'

    def __str__(self):
        return f"{self.category}"


class Credit_income(models.Model):
    category = models.ForeignKey(Filial,verbose_name="Qaysi filialga", on_delete=models.DO_NOTHING, default=None,null=True,related_name="kredit_income")
    dollar = models.IntegerField("Dollar",default=0,null=True,blank=True)
    income = models.IntegerField("So'm",default=0,null=True,blank=True)
    date = models.DateField("Vaqt",)


    class Meta:
        ordering = ["-id"]
        verbose_name = "Kredit income"
    
    def __str__(self):
        return f"{self.category}"


class Others(models.Model):
    category = models.ForeignKey(Filial,verbose_name='Boshqalar', on_delete=models.DO_NOTHING,default=None, null=True, related_name='others')
    income = models.IntegerField('Boshqalar uchun to\'lov', default=0,null=True,blank=True)
    description = models.TextField('Izoh')
    date = models.DateField('Vaqt')

    class Meta:
        verbose_name = 'Boshqalar uchun to\'lov'

    def __str__(self):
        return f"{self.category}"




class Incomes(models.Model):
    name = models.CharField("Xisob raqamlar nomi", max_length=50)
    slug = models.SlugField("*",unique=True)


    def get_url(self):
        return reverse("main:income_list", kwargs={"income_slug":self.slug,})
    
    
    def __str__(self):
        return "{}".format(self.name)




class Income_XRS(models.Model):
    category = models.ForeignKey(Filial,verbose_name="Qaysi fililalga", on_delete=models.DO_NOTHING, default=None,null=True,related_name="filial")
    income = models.ForeignKey(Incomes,verbose_name="Qayerga", on_delete=models.CASCADE, default=None,null=True,related_name="income")
    sum = models.IntegerField('Summa',null=True,default=0,blank=True)
    description = models.TextField("Izoh",)
    date = models.DateField("Vaqt", auto_now_add=True,)

    class Meta:
        ordering = ["-id"]
        verbose_name = "Xisob raqamga pul o'tkaz"

    def __str__(self):
        return f"{self.category}"






class Manag_add_gas(models.Model):
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.DO_NOTHING, default=None, null=True)
    category = models.ForeignKey(Filial,verbose_name="Manager_filiali", on_delete=models.DO_NOTHING, default=None, null=True, related_name='manager_filial')
    kalonka_1 = models.PositiveIntegerField('1 chi kalonka',default=0, null=True,blank=True)
    kalonka_2 = models.PositiveIntegerField('2 chi kalonka',default=0, null=True,blank=True)
    kalonka_3 = models.PositiveIntegerField('3 chi kalonka', default=0,null=True,blank=True)
    kalonka_4 = models.PositiveIntegerField('4 chi kalonka', default=0,null=True,blank=True)
    kalonka_5 = models.PositiveIntegerField('5 chi kalonka',default=0, null=True,blank=True)
    kalonka_6 = models.PositiveIntegerField('6 chi kalonka', default=0,null=True,blank=True)
    kalonka_7 = models.PositiveIntegerField('7 chi kalonka', default=0,null=True,blank=True)
    kalonka_8 = models.PositiveIntegerField('8 chi kalonka', default=0,null=True,blank=True)
    total_gas = models.PositiveIntegerField('Gaz xisoblagich',default=0, null=True, blank=True)
    remain_gas = models.PositiveIntegerField('Sotilgan gaz', default=0,null=True,blank=True)
    lose_gas = models.PositiveIntegerField("1.4 % yo'qotish",default=0,null=True,blank=True)
    gas = models.PositiveIntegerField("Gazni ta'ni",default=0,null=True,blank=True)
    total_sum = models.PositiveIntegerField('Sotilgan gaz puli',default=0, null=True,blank=True)
    date = models.DateField("Vaqt",)


    class Meta:
        ordering = ["-id"]
        verbose_name = "Zapravka sotgan gazi"
        verbose_name_plural = "Zapravka sotgan gazi"


    def __str__(self):
        return f"{self.category}"
    


    

class Manag_totals(models.Model):
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.DO_NOTHING, default=None, null=True)
    category = models.ForeignKey(Filial, verbose_name="Total_Filiali", on_delete=models.DO_NOTHING, default=None, null=True, related_name='total_filial')
    counter = models.PositiveIntegerField('Xisoblagich',default=0, null=True, blank=True)
    total_gas = models.PositiveIntegerField('Sotilgan gaz', default=0,null=True, blank=True)
    lose_gas = models.PositiveIntegerField('1,4% Yo\'qotish', default=0,null=True, blank=True)
    gas = models.PositiveIntegerField('Gazning ta\'ni',default=0, null=True, blank=True)
    sale_price = models.PositiveIntegerField('Gazning sotish narxi', default=0,null=True,blank=True)
    chec = models.PositiveIntegerField('Naqt',null=True, default=0,blank=True)
    card = models.PositiveIntegerField('Plastik karta',null=True, default=0,blank=True)
    card_uz = models.PositiveIntegerField('Uzcard karta',null=True, default=0,blank=True)
    card_humo = models.PositiveIntegerField('Humo karta',null=True, default=0,blank=True)
    sum_half = models.PositiveIntegerField('Daromat',default=0,null=True,blank=True)
    company = models.PositiveIntegerField('Tashkilotlar',)
    total_sum = models.PositiveIntegerField('Umumiy sovda',default=0,null=True,blank=True)
    date = models.DateField("Vaqt",)

    class Meta:
        ordering = ['-id']
        verbose_name = "Zapravka xisoboti"
        verbose_name_plural = "Zapravka xisoboti"


    def __str__(self):
        return f"{self.category}"



