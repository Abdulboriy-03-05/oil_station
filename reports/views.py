from django.shortcuts import render
from django.shortcuts import render,redirect
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
# Create your views here.

def home(request):  
    if request.user.is_staff:
        total_monay = 0
        total_buy_gas = 0
        total_sale_gas = 0
        obj = Filial.objects.all()
        totals = Main_XR.objects.all()
        yesterday = datetime.now() - timedelta(days=1)
        total_buy_gases = Addmaingas.objects.filter(date=yesterday)
        total_sale_gases = Manag_totals.objects.filter(date=yesterday) 


        for total in totals:
            total_monay += total.bill


        for total in total_buy_gases:
            total_buy_gas += total.last_gas


        for total_gas in total_sale_gases:
            total_sale_gas += total_gas.gas
            


        context = {
            "categories":obj,
            "total_monay":total_monay,
            "totals":totals,
            "total_buy_gas":total_buy_gas,
            "total_buy_gases":total_buy_gases,
            "total_sale_gas":total_sale_gas,
            "total_sale_gases":total_sale_gases.reverse(),
        }
        return render(request, 'index.html',context,)
    
    if request.user.is_authenticated:
        user = request.user
        manage = Manag_totals.objects.filter(user=user)
        yesterday = datetime.now() - timedelta(days=1)
        manage_yester = Manag_totals.objects.filter(user=user,date=yesterday)

        context = {
            "object":manage,
            "object_yesterdays":manage_yester,
        }
        return render(request, 'director.html',context,)
    else:
        return redirect ("/account/login")


def category_list(request, category_slug):
    main_today = 0
    other_today = 0
    obj = Filial.objects.all()
    category = Filial.objects.get(slug=category_slug)
    reports = Addmaingas.objects.filter(category=category)
    stations = Manag_totals.objects.filter(category=category)
    main_xr = Main_XR.objects.get(category=category)
    xudud_xr = Xududgaz_XR.objects.get(category=category)
    aksiz_xr = Aksiz_XR.objects.get(category=category)
    company = Company_XR.objects.get(category=category)
    cardit = Credit.objects.get(category=category)
    out_main = Main_XR_outcome.objects.filter(category=category,date=datetime.today())
    out_xudud = Xudud_XR_outcome.objects.filter(category=category)
    out_aksiz = Aksiz_XR_outcome.objects.filter(category=category)
    out_company = Company_XR_income.objects.filter(category=category)
    out_credit = Credit_income.objects.filter(category=category)
    others = Others.objects.filter(category=category,date=datetime.today())
    category_name = category_slug.capitalize()


    for main in out_main:
        main_today += main.outcome

    for other in others:
        other_today += other.income
    context = {
        "object_list":reports,
        "stations":stations,
        "categories":obj,
        'category_name': category_name,
        "main_xr":main_xr,
        "xudud_xr":xudud_xr,
        "aksiz_xr":aksiz_xr,
        "company":company,
        "cardit":cardit,
        "out_main":main_today,
        "out_xudud":out_xudud,
        "out_aksiz":out_aksiz,
        "out_company":out_company,
        "others":others,
        "other_today":other_today,
        "out_credit":out_credit,
        }
    return render(request, "cat.html", context)



def addmaingas(request):
    obj = Filial.objects.all()
    buy = Buyprice.objects.get()
    aksiz_tax = Aksiz.objects.get()
    if request.user.is_staff:
        if request.method == "POST":
            form = AddMainGasForm(request.POST)
            if form.is_valid():
                f = form.save(commit=False)
                cat = f.category
                gas_list = []
                f.author = request.user
                reports = Addmaingas.objects.filter(category=cat)
                for gas in reports:
                    gas_kub = int(gas.mian_gas)
                    gas_list.append(gas_kub)
                gas_main_remain = f.mian_gas - gas_list[0]
                f.last_gas = gas_main_remain

                f.buygasprice = buy.buyprice
                all_sum_buy = gas_main_remain * buy.buyprice
                f.buy_sum = all_sum_buy
                xudud_xr = Xududgaz_XR.objects.get(category=cat)
                xudud_xr_add = xudud_xr.bill
                xudud_add = xudud_xr_add - all_sum_buy
                xudud_xr.bill = xudud_add
                xudud_xr.save()

                xudud_xr_outcome = Xudud_XR_outcome.objects.create(category=cat,outcome = all_sum_buy)
                xudud_xr_outcome.save()

                f.aksiz = aksiz_tax.aksiz
                all_sum_aksiz = gas_main_remain * aksiz_tax.aksiz
                f.aksiz_sum = all_sum_aksiz
                aksiz_xr = Aksiz_XR.objects.get(category=cat)
                aksiz_xr_add = aksiz_xr.bill
                aksiz_add = aksiz_xr_add - all_sum_aksiz
                aksiz_xr.bill = aksiz_add
                aksiz_xr.save()

                aksiz_xr_outcome = Aksiz_XR_outcome.objects.create(category=cat,outcome = all_sum_aksiz)
                aksiz_xr_outcome.save()



                yesterday = datetime.now() - timedelta(days=1)
                f.date = yesterday
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
    



def addincome(request):
    obj = Filial.objects.all()
    send = Send.objects.get()
    if request.user.is_staff:
        if request.method == "POST":
            form = AddIncomeForm(request.POST)
            if form.is_valid():
                f = form.save(commit=False)
                cat = f.category
                sum = f.sum
                if str(f.income) == 'Xudud gaz':
                    print("Xudud gazga qo'shildi")
                    send_tax = send.send_tax
                    main_xr = Main_XR.objects.get(category=cat)
                    minus_xr = main_xr.bill
                    tax = sum / 100
                    tax_1 = tax * send_tax
                    tax_2 = sum + tax_1
                    main_minus = minus_xr - tax_2
                    main_xr.bill = main_minus
                    main_xr.save()
                    main_outcome = Main_XR_outcome.objects.create(category=cat,outcome = tax_2,description=f.description)
                    main_outcome.save()


                    xudud_xr = Xududgaz_XR.objects.get(category=cat)
                    xudud_xr_add = xudud_xr.bill
                    xudud_add = xudud_xr_add + sum
                    xudud_xr.bill = xudud_add
                    xudud_xr.save()

                    xudud_xr_income = Xudud_XR_income.objects.create(category=cat,income = sum)
                    xudud_xr_income.save()
                else:
                    print("Xudud ga qo'shilmadi")

                if str(f.income) == 'Aksiz':
                    print("Aksiz soliq ga qo'shildo")

                    send_tax = send.send_tax
                    main_xr = Main_XR.objects.get(category=cat)
                    minus_xr = main_xr.bill
                    tax = sum / 100
                    tax_1 = tax * send_tax
                    tax_2 = sum + tax_1
                    main_minus = minus_xr - tax_2
                    main_xr.bill = main_minus
                    main_xr.save()
                    main_outcome = Main_XR_outcome.objects.create(category=cat,outcome = tax_2,description=f.description)
                    main_outcome.save()

                
                    aksiz_xr = Aksiz_XR.objects.get(category=cat)
                    aksiz_xr_add = aksiz_xr.bill
                    aksiz_add = aksiz_xr_add + sum
                    aksiz_xr.bill = aksiz_add
                    aksiz_xr.save()

                    aksiz_xr_income = Aksiz_XR_income.objects.create(category=cat,income = sum)
                    aksiz_xr_income.save()
                else: 
                    print("Aksiz ga qo'shilmadi")

                    
                if str(f.income) == 'Kredit':
                    print("Kredit ga qo'shilda")

                    send_tax = send.send_tax
                    main_xr = Main_XR.objects.get(category=cat)
                    minus_xr = main_xr.bill
                    tax = sum / 100
                    tax_1 = tax * send_tax
                    tax_2 = sum + tax_1
                    main_minus = minus_xr - tax_2
                    main_xr.bill = main_minus
                    main_xr.save()
                    main_outcome = Main_XR_outcome.objects.create(category=cat,outcome = tax_2,description=f.description)
                    main_outcome.save()


                    credit_xr = Credit.objects.get(category=cat)
                    credit_xr_add = credit_xr.bill
                    credit_add = credit_xr_add - sum
                    credit_xr.bill = credit_add
                    credit_xr.save()

                    aksiz_xr_income = Credit_income.objects.create(category=cat,income = sum)
                    aksiz_xr_income.save()
                else:
                    print("Kredit ga qo'shilmadi")


                if str(f.income) == 'Boshqalar':
                    print("Boshqalar ga qo'shilda")

                    others_income = Others.objects.create(category=cat,income = sum,description=f.description)
                    others_income.save()
                else:
                    print("Boshqalar ga qo'shilmadi")
                f.save()


                return redirect('/')
        else:
            form = AddIncomeForm()
            print("NOT " * 5)
        
        context = {
            "for":form,
            "categories":obj
        }

        return render(request, "add_to_income.html", context)

    else:
        return redirect('/')





def station_add_gas(request):
    lose = Losegas.objects.get()
    sale_sum = Saleprice.objects.get()
    if request.user.username == 'Sanoat tranzit':
        number = request.user.number
        number_2 = str(number)
        category = Filial.objects.get(id=number_2)
        if request.method == "POST":
            form = Stationsalegas_8(request.POST)
            if form.is_valid():
                f = form.save(commit=False)
                user = request.user
                f.user = user
                f.category = category
                x_1 = f.kalonka_1 + f.kalonka_2
                x_2 =  f.kalonka_3 + x_1
                x_3 =  f.kalonka_4 + x_2
                x_4 =  f.kalonka_5 + x_3
                x_5 =  f.kalonka_6 + x_4
                x_6 =  f.kalonka_7 + x_5
                x_7 =  f.kalonka_8 + x_6
                f.total_gas = x_7
                remain_list = []
                remain_gas = Manag_add_gas.objects.filter(user=user)
                for x in remain_gas:
                    y = int(x.total_gas)
                    remain_list.append(y)
                remain_gas_1 = x_7 - remain_list[0]
                f.remain_gas = remain_gas_1

                lose_gas_1 = remain_gas_1 / 100
                lose_gas_2 = lose_gas_1 * lose.losegas
                f.lose_gas = lose_gas_2

                lose_end = remain_gas_1 - lose_gas_2
                f.gas = lose_end
                
                total_sum = lose_end * sale_sum.saleprice
                total_money = Manag_add_card.objects.create(user=user, category=category,counter=x_7,total_gas_card=remain_gas_1,lose_gas=lose_gas_2,gas=lose_end,total_sum=total_sum) 
                total_money.save()
                f.save()

            return redirect('main:add_card_income')
        
        else:
            form = Stationsalegas_8()
            print("NOT " * 5)
        
        context = {
            "form":form,
        }

        return render(request, "add_station_gas.html", context)

    if request.user.is_authenticated:
        number = request.user.number
        number_2 = str(number)
        category = Filial.objects.get(id=number_2)
        if request.method == "POST":
            form = Stationsalegas_6(request.POST)
            if form.is_valid():
                f = form.save(commit=False)
                user = request.user
                f.user = user
                f.category = category
                x_1 = f.kalonka_1 + f.kalonka_2
                x_2 =  f.kalonka_3 + x_1
                x_3 =  f.kalonka_4 + x_2
                x_4 =  f.kalonka_5 + x_3
                x_5 =  f.kalonka_6 + x_4
                f.total_gas = x_5
                remain_list = []
                remain_gas = Manag_add_gas.objects.filter(user=user)
                for x in remain_gas:
                    y = int(x.total_gas)
                    remain_list.append(y)
                remain_gas_1 = x_5 - remain_list[0]
                f.remain_gas = remain_gas_1

                lose_gas_1 = remain_gas_1 / 100
                lose_gas_2 = lose_gas_1 * lose.losegas
                f.lose_gas = lose_gas_2

                lose_end = remain_gas_1 - lose_gas_2
                f.gas = lose_end

                total_sum = lose_end * sale_sum.saleprice
                total_money = Manag_add_card.objects.create(user=user, category=category,counter=x_5,total_gas_card=remain_gas_1,lose_gas=lose_gas_2,gas=lose_end,total_sum=total_sum) 
                total_money.save()
                f.save()

            return redirect('main:add_card_income')
        
        else:
            form = Stationsalegas_6()
            print("NOT " * 5)
        
        context = {
            "form":form,
        }

        return render(request, "add_station_gas.html", context)

    else:
        print("Boshqa userlar")





def add_card_income(request):
    sale = Saleprice.objects.get()
    user = request.user
    totals = Manag_add_card.objects.filter(user=user)
    user = request.user
    if request.user.is_authenticated:
        if request.method == "POST":
            form = Stationaddgas(request.POST)
            if form.is_valid():
                f = form.save(commit=False)
                f.user = user
                counter = []
                total_gas = []
                lose_gas = []
                gas = []
                total_sum = []
                for total in totals:
                    f.category = total.category
                    counter.append(int(total.counter))
                    total_gas.append(int(total.total_gas_card))
                    lose_gas.append(int(total.lose_gas))
                    gas.append(int(total.gas))
                    total_sum.append(int(total.total_sum))
                f.counter = counter[0]
                f.total_gas = total_gas[0]
                f.lose_gas = lose_gas[0]
                f.gas = gas[0]
                f.total_sum = total_sum[0]
                f.sale_price = sale.saleprice
                sum_half = total_sum[0] - f.company
                f.sum_half = sum_half
                check = sum_half - f.card
                f.chec = check

                cat = f.category
                main_xr = Main_XR.objects.get(category=cat)
                main_xr_add = main_xr.bill
                main_add = main_xr_add + sum_half
                print(main_add)
                main_xr.bill = main_add
                main_xr.save()
                
                main_xr_income = Main_XR_income.objects.create(category=cat,income = sum_half)
                main_xr_income.save()

                company = Company_XR.objects.get(category=cat)
                minus_xr = company.bill
                company_minus = minus_xr + f.company
                company.bill = company_minus
                company.save()

                company_income = Company_XR_income.objects.create(category=cat,income=f.company)
                company_income.save()

                f.date = datetime.today()
                f.save()
            return redirect('/')
        else:
            form = Stationaddgas()
            print("NOT " * 5)

        context = {
            "totals":totals,
            "form":form
        }
        return render(request, "add_card_incomes.html", context)
    else:
        return redirect('/')