from django.shortcuts import render
from django.shortcuts import render,redirect
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from typing import List
# Create your views here.

def home(request):
    obj = Filial.objects.all()
    if request.user.is_staff:
        context = {
            "categories":obj
        }
        return render(request, 'index.html',context,)
    if request.user.is_authenticated:
        return render(request, 'director.html')
    else:
        return redirect ("/account/login")


def category_list(request, category_slug):
    obj = Filial.objects.all()
    category = Filial.objects.get(slug=category_slug)
    reports = Addmaingas.objects.filter(category=category)
    main_xr = Main_XR.objects.get(category=category)
    xudud_xr = Xududgaz_XR.objects.get(category=category)
    category_name = category_slug.capitalize()
    context = {
        "object_list":reports,
        "categories":obj,
        'category_name': category_name,
        "main_xr":main_xr,
        "xudud_xr":xudud_xr,
        }
    return render(request, "cat.html", context)



def addmaingas(request):
    obj = Filial.objects.all()
    sale = Saleprice.objects.all()
    buy = Buyprice.objects.all()
    lose = Losegas.objects.all()
    aksiz_tax = Aksiz.objects.all()
    if request.user.is_staff:
        if request.method == "POST":
            form = AddMainGasForm(request.POST)
            if form.is_valid():
                f = form.save(commit=False)
                cat = f.category
                gas_list = []
                reports = Addmaingas.objects.filter(category=cat)
                for gas in reports:
                    gas_kub = int(gas.mian_gas)
                    gas_list.append(gas_kub)
                gas_main_remain = f.mian_gas - gas_list[0]
                f.last_gas = gas_main_remain

                for y in lose:
                    f.author = request.user
                    lose_gas_1 = f.last_gas / 100
                    lose_gas_2 = lose_gas_1 * y.losegas
                    f.lose = lose_gas_2
                    remain_gas = f.last_gas - lose_gas_2
                    f.remain = remain_gas
    
                for i in sale:
                    f.salegasprice = i.saleprice
                    all_sum_sale = remain_gas * i.saleprice
                    f.sale_sum = all_sum_sale
                main_xr = Main_XR.objects.get(category=cat)
                main_xr_add = main_xr.main
                main_add = main_xr_add + all_sum_sale
                print(main_add)
                main_xr.main = main_add
                main_xr.save()
                
                main_xr_income = Main_XR_income.objects.create(category=cat,income = main_add)
                main_xr_income.save()

                for x in buy:
                    f.buygasprice = x.buyprice
                    all_sum_buy = remain_gas * x.buyprice
                    f.buy_sum = all_sum_buy
                xudud_xr = Xududgaz_XR.objects.get(category=cat)
                xudud_xr_add = xudud_xr.bill
                xudud_add = xudud_xr_add - all_sum_buy
                print(xudud_add)
                xudud_xr.bill = xudud_add
                xudud_xr.save()

                xudud_xr_outcome = Xudud_XR_income.objects.create(category=cat,outcome =xudud_add)
                xudud_xr_outcome.save()

                for a in aksiz_tax:
                    f.aksiz = a.aksiz
                    all_sum_aksiz = remain_gas * a.aksiz
                    f.aksiz_sum = all_sum_aksiz
                aksiz_xr = Aksiz_XR.objects.get(category=cat)
                aksiz_xr_add = aksiz_xr.bill
                aksiz_add = aksiz_xr_add - all_sum_aksiz
                aksiz_xr.bill = aksiz_add
                aksiz_xr.save()

                f.save()

                return redirect('/')
        else:
            form = AddMainGasForm()
            print("NOT " * 5)
        
        context = {
            "for":form,
            "categories":obj,
            }
        return render(request, "add_to_gas.html",context)

    else:
        return redirect('/')
    
