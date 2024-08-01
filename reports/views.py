from django.shortcuts import render
from django.shortcuts import render,redirect
from datetime import datetime, timedelta
from django.utils.timezone import now
from .forms import *
from .models import *
# Create your views here.

def home(request):
    if request.user.is_staff:
        total_monay = 0
        total_buy_gas = 0
        total_sale_gas = 0
        obj = Filial.objects.all()
        today =  datetime.today()
        yesterday = datetime.now() - timedelta(days=1)
        total_buy_gases = Addmaingas.objects.select_related('category').filter(date=yesterday)
        total_sale_gases = Manag_totals.objects.select_related('category').filter(date=yesterday)
        main_xr = Main_XR.objects.select_related('category').all()
        main_gas = Xududgaz_XR.objects.select_related('category').all()
        main_aksiz = Aksiz_XR.objects.select_related('category').all()
        main_elector = Elector_XR.objects.select_related('category').all()
        main_company = Company_XR.objects.select_related('category').all()
        main_credit = Credit.objects.select_related('category').all()
                        
        for xr in main_xr:
            if str(xr.category) == "Nasirullo xoji":
                cat_nas = xr.category
                dev_nas_xr = ''.join(str(xr.date))
                if str(xr.date) in str(yesterday):
                    nas_total_yes = xr.bill
                    # print(xr.date)
                    # print(nas_total_yes)
                elif str(xr.date) in str(today):
                    money_nas = xr.bill
                else:
                    nas_total_yes = 0
                    money_nas = 0
        

            if str(xr.category) == "Sanoat tranzit":
                cat_san = xr.category
                dev_san_xr = ''.join(str(xr.date))
                if str(xr.date) in str(yesterday):
                    san_total_yes = xr.bill
                    # print(xr.date)
                    # print(san_total_yes)
                elif str(xr.date) in str(today):
                    money_san = xr.bill
                else:
                    san_total_yes = 0
                    money_san = 0
            
            if str(xr.category) == "Parfum distibyuter":
                cat_par = xr.category
                dev_par_xr = ''.join(str(xr.date))
                if str(xr.date) in str(yesterday):
                    par_total_yes = xr.bill
                    # print(xr.date)
                    # print(par_total_yes)
                elif str(xr.date) in str(today):
                    money_par = xr.bill
                else:
                    par_total_yes = 0
                    money_par = 0

        if dev_nas_xr not in str(today):
            xr = Main_XR.objects.create(category=cat_nas,bill = nas_total_yes, date=today)
            xr.save()

        if dev_san_xr not in str(today):
            xr = Main_XR.objects.create(category=cat_san,bill = san_total_yes, date=today)
            xr.save()

        if dev_par_xr not in str(today):
            xr = Main_XR.objects.create(category=cat_par,bill = par_total_yes, date=today)
            xr.save()
            return redirect("/")

        total_mon = money_nas + money_san
        total_monay = money_par + total_mon


        for gas in main_gas:
            if str(gas.category) == "Nasirullo xoji":
                cat_nas = gas.category
                dev_nas_gas = ''.join(str(gas.date))
                if str(gas.date) in str(yesterday):
                    nas_gas_yes = gas.bill
                    # print(gas.date)
                    # print(nas_gas_yes)
                else:
                    nas_gas_yes = 0
            if str(gas.category) == "Sanoat tranzit":
                cat_san = gas.category
                dev_san_gas = ''.join(str(gas.date))
                if str(gas.date) in str(yesterday):
                    san_gas_yes = gas.bill
                    # print(gas.date)
                    # print(san_gas_yes)
                else:
                    san_gas_yes = 0
            if str(gas.category) == "Parfum distibyuter":
                cat_par = gas.category
                dev_par_gas = ''.join(str(gas.date))
                if str(gas.date) in str(yesterday):
                    par_gas_yes = gas.bill
                    # print(gas.date)
                    # print(par_gas_yes)
                else:
                    par_gas_yes = 0

        if dev_nas_gas not in str(today):
            gases = Xududgaz_XR.objects.create(category=cat_nas,bill = nas_gas_yes, date=today)
            gases.save()

        if dev_san_gas not in str(today):
            gases = Xududgaz_XR.objects.create(category=cat_san,bill = san_gas_yes, date=today)
            gases.save()

        if dev_par_gas not in str(today):
            gases = Xududgaz_XR.objects.create(category=cat_par,bill = par_gas_yes, date=today)
            gases.save()



        for ak in main_aksiz:
            if str(ak.category) == "Nasirullo xoji":
                cat_nas = ak.category
                dev_nas_ak = ''.join(str(ak.date))
                if str(ak.date) in str(yesterday):
                    nas_ak_yes = ak.bill
                    # print(ak.date)
                    # print(nas_ak_yes)
                else:
                    nas_ak_yes = 0
            if str(ak.category) == "Sanoat tranzit":
                cat_san = ak.category
                dev_san_ak = ''.join(str(ak.date))
                if str(ak.date) in str(yesterday):
                    san_ak_yes = ak.bill
                    # print(ak.date)
                    # print(san_ak_yes)
                else:
                    san_ak_yes = 0
            if str(ak.category) == "Parfum distibyuter":
                cat_par = ak.category
                dev_par_ak = ''.join(str(ak.date))
                if str(ak.date) in str(yesterday):
                    par_ak_yes = ak.bill
                    # print(ak.date)
                    # print(par_ak_yes)
                else:
                    par_ak_yes = 0

        if dev_nas_ak not in str(today):
            aks = Aksiz_XR.objects.create(category=cat_nas,bill = nas_ak_yes, date=today)
            aks.save()

        if dev_san_ak not in str(today):
            aks = Aksiz_XR.objects.create(category=cat_san,bill = san_ak_yes, date=today)
            aks.save()

        if dev_par_ak not in str(today):
            aks = Aksiz_XR.objects.create(category=cat_par,bill = par_ak_yes, date=today)
            aks.save()

            


        for elec in main_elector:
            if str(elec.category) == "Nasirullo xoji":
                cat_nas = elec.category
                dev_nas_elec = ''.join(str(elec.date))
                if str(elec.date) in str(yesterday):
                    nas_elec_yes = elec.bill
                    # print(elec.date)
                    # print(nas_elec_yes)
                else:
                    nas_elec_yes = 0
            if str(elec.category) == "Sanoat tranzit":
                cat_san = elec.category
                dev_san_elec = ''.join(str(elec.date))
                if str(elec.date) in str(yesterday):
                    san_elec_yes = elec.bill
                    # print(elec.date)
                    # print(san_elec_yes)
                else:
                    san_elec_yes = 0
            if str(elec.category) == "Parfum distibyuter":
                cat_par = elec.category
                dev_par_elc = ''.join(str(elec.date))
                if str(elec.date) in str(yesterday):
                    par_elec_yes = elec.bill
                    # print(elec.date)
                    # print(par_elec_yes)
                else:
                    par_elec_yes = 0

        if dev_nas_elec not in str(today):
            main_elec = Elector_XR.objects.create(category=cat_nas,bill = nas_elec_yes, date=today)
            main_elec.save()

        if dev_san_elec not in str(today):
            main_elec = Elector_XR.objects.create(category=cat_san,bill = san_elec_yes, date=today)
            main_elec.save()

        if dev_par_elc not in str(today):
            main_elec = Elector_XR.objects.create(category=cat_par,bill = par_elec_yes, date=today)
            main_elec.save()


        today_1 = today.strftime('%d')
        print(type(str(today_1)))
        if str(today_1) in '01':
            for com in main_company:
                if str(com.category) == "Nasirullo xoji":
                    cat_nas = com.category
                    dev_nas_com = ''.join(str(com.date))
                    nas_com_yes = 0
                    print(nas_com_yes)
                if str(com.category) == "Sanoat tranzit":
                    cat_san = com.category
                    dev_san_com = ''.join(str(com.date))
                    san_com_yes = 0            
                    print(san_com_yes)
                if str(com.category) == "Parfum distibyuter":
                    cat_par = com.category
                    dev_par_com = ''.join(str(com.date))
                    par_com_yes = 0
                    print(par_com_yes)

            if dev_nas_com not in str(today):
                main_com = Company_XR.objects.create(category=cat_nas,bill = nas_com_yes, date=today)
                main_com.save()

            if dev_san_com not in str(today):
                main_com = Company_XR.objects.create(category=cat_san,bill = san_com_yes, date=today)
                main_com.save()

            if dev_par_com not in str(today):
                main_com = Company_XR.objects.create(category=cat_par,bill = par_com_yes, date=today)
                main_com.save()
            print(today_1)
        else:
            print("Bugun emas")
            for com in main_company:
                if str(com.category) == "Nasirullo xoji":
                    cat_nas = com.category
                    dev_nas_com = ''.join(str(com.date))
                    if str(com.date) in str(yesterday):
                        nas_com_yes = com.bill
                        # print(com.date)
                        # print(nas_com_yes)
                    else:
                        nas_com_yes = 0
                if str(com.category) == "Sanoat tranzit":
                    cat_san = com.category
                    dev_san_com = ''.join(str(com.date))
                    if str(com.date) in str(yesterday):
                        san_com_yes = com.bill
                        # print(com.date)
                        # print(san_com_yes)
                    else:
                        san_com_yes = 0
                if str(com.category) == "Parfum distibyuter":
                    cat_par = com.category
                    dev_par_com = ''.join(str(com.date))
                    if str(com.date) in str(yesterday):
                        par_com_yes = com.bill
                        # print(com.date)
                        # print(par_com_yes)
                    else:
                        par_com_yes = 0

            if dev_nas_com not in str(today):
                main_com = Company_XR.objects.create(category=cat_nas,bill = nas_com_yes, date=today)
                main_com.save()

            if dev_san_com not in str(today):
                main_com = Company_XR.objects.create(category=cat_san,bill = san_com_yes, date=today)
                main_com.save()

            if dev_par_com not in str(today):
                main_com = Company_XR.objects.create(category=cat_par,bill = par_com_yes, date=today)
                main_com.save()



        for cred in main_credit:
            if str(cred.category) == "Nasirullo xoji":
                cat_nas = cred.category
                dev_nas_cred = ''.join(str(cred.date))
                if str(cred.date) in str(yesterday):
                    nas_cred_yes = cred.bill
                    # print(cred.date)
                    # print(nas_cred_yes)
                else:
                    nas_cred_yes = 0
            if str(cred.category) == "Sanoat tranzit":
                cat_san = cred.category
                dev_san_cred = ''.join(str(cred.date))
                if str(cred.date) in str(yesterday):
                    san_cred_yes = cred.bill
                    # print(cred.date)
                    # print(san_cred_yes)
                else:
                    san_cred_yes = 0
            if str(cred.category) == "Parfum distibyuter":
                cat_par = cred.category
                dev_par_cred = ''.join(str(cred.date))
                if str(cred.date) in str(yesterday):
                    par_cred_yes = cred.bill
                    # print(cred.date)
                    # print(par_cred_yes)
                else:
                    par_cred_yes = 0

        if dev_nas_cred not in str(today):
            main_com = Credit.objects.create(category=cat_nas,bill = nas_cred_yes, date=today)
            main_com.save()

        if dev_san_cred not in str(today):
            main_com = Credit.objects.create(category=cat_san,bill = san_cred_yes, date=today)
            main_com.save()

        if dev_par_cred not in str(today):
            main_com = Credit.objects.create(category=cat_par,bill = par_cred_yes, date=today)
            main_com.save()




        main_nasirullo = 0
        main_sanoat = 0
        main_parfum = 0


        for x in total_buy_gases:
            cat = x.category
            
            if str(cat) in "Nasirullo xoji":
                main_nasirullo = x.last_gas
            if str(cat) in "Sanoat tranzit":
                main_sanoat = x.last_gas
            if str(cat) in "Parfum distibyuter":
                main_parfum = x.last_gas

        gas_nasirullo = 0
        gas_sanoat = 0
        gas_parfum = 0
        for x in total_sale_gases:
            cat = x.category
            
            if str(cat) in "Nasirullo xoji":
                gas_nasirullo = x.gas
            if str(cat) in "Sanoat tranzit":
                gas_sanoat = x.gas
            if str(cat) in "Parfum distibyuter":
                gas_parfum = x.gas

            
        
            
        for total in total_buy_gases:
            total_buy_gas += total.last_gas


        for total_gas in total_sale_gases:
            total_sale_gas += total_gas.gas
        

        yesterday_before = datetime.now() - timedelta(days=2)
        total_buy_gases_yes = Addmaingas.objects.select_related('category').filter(date=yesterday_before)
        
        add = 0

        for x in total_buy_gases_yes:
            cat = x.category
            
            if str(cat) in "Nasirullo xoji":
                add += 1
            if str(cat) in "Sanoat tranzit":
                add += 1
            if str(cat) in "Parfum distibyuter":
                add += 1

        print(add)
        context = {
            "add":add,
            "categories":obj,
            "total_monay":total_monay,
            "nas_totals":money_nas,
            "san_totals":money_san,
            "par_totals":money_par,
            "total_buy_gas":total_buy_gas,
            "total_buy_gases":total_buy_gases,
            "total_sale_gas":total_sale_gas,
            "main_nasirullo":main_nasirullo,
            "main_sanoat":main_sanoat,
            "main_parfum":main_parfum,
            "gas_nasirullo":gas_nasirullo,
            "gas_sanoat":gas_sanoat,
            "gas_parfum":gas_parfum,
        }
        return render(request, 'index.html',context,)
    
    if request.user.is_authenticated:
        user = request.user
        manage = Manag_totals.objects.select_related('category').filter(user=user)
        yesterday = datetime.now() - timedelta(days=1)
        manage_yester = Manag_totals.objects.select_related('category').filter(user=user,date=yesterday)

        context = {
            "object":manage,
            "object_yesterdays":manage_yester,
        }
        return render(request, 'director.html',context,)
    else:
        return redirect ("/account/login")


def nasirullo_outcome(request):
    category_1 = Filial.objects.all()
    category = Filial.objects.get(id=1)
    today = datetime.today()
    current_month = now().month
    this_month = Main_XR_outcome.objects.select_related('category').filter(category=category,date__month=current_month)
    total_otherday = 0
    otherday_outcome = []
    otherday_descript = []
    otherday_date = []

    total_today = 0
    today_outcome = []
    today_descript = []
    today_date = []



    for y in this_month:
        if str(y.date) not in str(today):
            otherday_outcome.append(y.outcome)
            otherday_descript.append(y.description)
            otherday_date.append(y.date)
            # print(y.outcome,y.description, y.date)
        if str(y.date) in str(today):
            # print("Today",today_out.outcome,today_out.description)
            today_outcome.append(y.outcome)
            today_descript.append(y.description)
            today_date.append(y.date)

    for otherday_out in otherday_outcome:
        total_otherday += otherday_out


    for today_out in today_outcome:
        total_today += today_out
    total = total_otherday + total_today

    context = {
        "total":total,
        "categories":category_1,
        "cattitle":category,
        "otherday_outcome":otherday_outcome,
        "otherday_descript":otherday_descript,
        "otherday_date":otherday_date,
        "total_otherday":total_otherday,


        "today_outcome":today_outcome,
        "today_descript":today_descript,
        "today_date":today_date,
        "total_today":total_today,

    }

    return render(request, "mainout.html" , context)



def sanoat_outcome(request):
    category_1 = Filial.objects.all()
    category = Filial.objects.get(id=2)
    today = datetime.today()
    current_month = now().month
    this_month = Main_XR_outcome.objects.filter(category=category,date__month=current_month)
    total_otherday = 0
    otherday_outcome = []
    otherday_descript = []
    otherday_date = []

    total_today = 0
    today_outcome = []
    today_descript = []
    today_date = []


    for y in this_month:
        if str(y.date) not in str(today):
            otherday_outcome.append(y.outcome)
            otherday_descript.append(y.description)
            otherday_date.append(y.date)
            # print(y.outcome,y.description, y.date)
        if str(y.date) in str(today):
            # print("Today",today_out.outcome,today_out.description)
            today_outcome.append(y.outcome)
            today_descript.append(y.description)
            today_date.append(y.date)
            

    for otherday_out in otherday_outcome:
        total_otherday += otherday_out


    for today_out in today_outcome:
        total_today += today_out

    total = total_otherday + total_today
    context = {
        "total":total,
        "categories":category_1,
        "cattitle":category,
        "otherday_outcome":otherday_outcome,
        "otherday_descript":otherday_descript,
        "otherday_date":otherday_date,
        "total_otherday":total_otherday,


        "today_outcome":today_outcome,
        "today_descript":today_descript,
        "today_date":today_date,
        "total_today":total_today,

    }

    return render(request, "mainout.html" , context)




def parfum_outcome(request):
    category_1 = Filial.objects.all()
    category = Filial.objects.get(id=3)
    today = datetime.today()
    current_month = now().month
    this_month = Main_XR_outcome.objects.select_related('category').filter(category=category,date__month=current_month)
    total_otherday = 0
    otherday_outcome = []
    otherday_descript = []
    otherday_date = []

    total_today = 0
    today_outcome = []
    today_descript = []
    today_date = []


    for y in this_month:
        if str(y.date) not in str(today):
            otherday_outcome.append(y.outcome)
            otherday_descript.append(y.description)
            otherday_date.append(y.date)
            # print(y.outcome,y.description, y.date)
        if str(y.date) in str(today):
            # print("Today",today_out.outcome,today_out.description)
            today_outcome.append(y.outcome)
            today_descript.append(y.description)
            today_date.append(y.date)
            

    for otherday_out in otherday_outcome:
        total_otherday += otherday_out


    for today_out in today_outcome:
        total_today += today_out

    total = total_otherday + total_today
    context = {
        "total":total,
        "categories":category_1,
        "cattitle":category,
        "otherday_outcome":otherday_outcome,
        "otherday_descript":otherday_descript,
        "otherday_date":otherday_date,
        "total_otherday":total_otherday,


        "today_outcome":today_outcome,
        "today_descript":today_descript,
        "today_date":today_date,
        "total_today":total_today,

    }

    return render(request, "mainout.html" , context)



def nasirullo_company(request):
    category_1 = Filial.objects.all()
    category = Filial.objects.get(id=1)
    today = datetime.today()
    current_month = now().month
    this_month = Company_XR.objects.select_related('category').filter(category=category,date__month=current_month)
    this_month_income = Company_XR_income.objects.select_related("category").filter(category=category,date__month=current_month)
    otherday_income = []
    otherday_date = []
    otherday_main = []

    today_income = []
    today_date = []
    today_main = []

    for y in this_month:
        if str(y.date) not in str(today):
            otherday_main.append(y.bill)
            print(y.bill, y.date)
        if str(y.date) in str(today):
            today_main.append(y.bill)
            print("Today",y.bill,y.date)

    for y in this_month_income:
        if str(y.date) not in str(today):
            otherday_income.append(y.income)
            otherday_date.append(y.date)
            print(y.income, y.date)
        if str(y.date) in str(today):
            today_income.append(y.income)
            today_date.append(y.date)
            print("Today",y.income,y.date)

    context = {
        "categories":category_1,
        "cattitle":category,
        "otherday_main":otherday_main[::-1],
        "otherday_income":otherday_income,
        "otherday_date":otherday_date,


        "today_main":today_main,
        "today_income":today_income,
        "today_date":today_date,

    }

    return render(request, "company.html" , context)




def parfum_company(request):
    category_1 = Filial.objects.all()
    category = Filial.objects.get(id=3)
    today = datetime.today()
    current_month = now().month
    this_month = Company_XR.objects.select_related('category').filter(category=category,date__month=current_month)
    this_month_income = Company_XR_income.objects.select_related("category").filter(category=category,date__month=current_month)
    otherday_income = []
    otherday_date = []
    otherday_main = []

    today_income = []
    today_date = []
    today_main = []

    for y in this_month:
        if str(y.date) not in str(today):
            otherday_main.append(y.bill)
            print(y.bill, y.date)
        if str(y.date) in str(today):
            today_main.append(y.bill)
            print("Today",y.bill,y.date)

    for y in this_month_income:
        if str(y.date) not in str(today):
            otherday_income.append(y.income)
            otherday_date.append(y.date)
            print(y.income, y.date)
        if str(y.date) in str(today):
            today_income.append(y.income)
            today_date.append(y.date)
            print("Today",y.income,y.date)


    context = {
        "categories":category_1,
        "cattitle":category,
        "otherday_main":otherday_main[::-1],
        "otherday_income":otherday_income,
        "otherday_date":otherday_date,


        "today_main":today_main,
        "today_income":today_income,
        "today_date":today_date,

    }

    return render(request, "company.html" , context)


def main_reports_nas(request):
    category = Filial.objects.all()
    for cat in category:
        if str(cat) in "Nasirullo xoji":
            categ = cat
    current_month = now().month
    main_income = Main_XR_income.objects.select_related('category').filter(category=categ,date__month=current_month)
    main_outcome = Main_XR_outcome.objects.select_related('category').filter(category=categ,date__month=current_month)
    gases = Xudud_XR_income.objects.select_related('category').filter(category=categ,date__month=current_month)
    aksizes = Aksiz_XR_income.objects.select_related('category').filter(category=categ,date__month=current_month)
    elektors = Elector_XR_income.objects.select_related('category').filter(category=categ,date__month=current_month)
    kredits = Credit_income.objects.select_related('category').filter(category=categ,date__month=current_month)
    debts = Debts.objects.select_related('category').filter(category=categ,date__month=current_month)
    others = Others.objects.select_related('category').filter(category=categ,date__month=current_month)
    income_total = 0
    outcome_total = 0
    gas_total = 0
    aksiz_total = 0
    elektor_total = 0
    kredit_total = 0
    other_total = 0
    debt_total = 0

    for y in main_income:
        income_total += y.income

    for y in main_outcome:
        outcome_total += y.outcome

    for gas in gases:
        gas_total += gas.income

    for aksiz in aksizes:
        aksiz_total += aksiz.income

    for elektor in elektors:
        elektor_total += elektor.income

    for kredit in kredits:
        kredit_total += kredit.income

    for other in others:
        other_total += other.income

    for debt in debts:
        print(debt.debt)
        debt_total += debt.debt

    context = {
        "categories":category,
        "cattitle":categ,
        "main_income":main_income,
        "main_outcome":main_outcome,
        "income_total":income_total,
        "outcome_total":outcome_total,
        "gas_total":gas_total,
        "aksiz_total":aksiz_total,
        "elektor_total":elektor_total,
        "kredit_total":kredit_total,
        "other_total":other_total,
        "debt_total":debt_total,
    }

    return render(request, 'main_bill.html',context)


def main_reports_san(request):
    category = Filial.objects.all()
    for cat in category:
        if str(cat) in "Sanoat tranzit":
            categ = cat
    current_month = now().month
    main_income = Main_XR_income.objects.select_related('category').filter(category=categ,date__month=current_month)
    main_outcome = Main_XR_outcome.objects.select_related('category').filter(category=categ,date__month=current_month)
    gases = Xudud_XR_income.objects.select_related('category').filter(category=categ,date__month=current_month)
    aksizes = Aksiz_XR_income.objects.select_related('category').filter(category=categ,date__month=current_month)
    elektors = Elector_XR_income.objects.select_related('category').filter(category=categ,date__month=current_month)
    kredits = Credit_income.objects.select_related('category').filter(category=categ,date__month=current_month)
    debts = Debts.objects.select_related('category').filter(category=categ,date__month=current_month)
    others = Others.objects.select_related('category').filter(category=categ,date__month=current_month)
    income_total = 0
    outcome_total = 0
    gas_total = 0
    aksiz_total = 0
    elektor_total = 0
    kredit_total = 0
    other_total = 0
    debt_total = 0

    for y in main_income:
        income_total += y.income

    for y in main_outcome:
        outcome_total += y.outcome

    for gas in gases:
        gas_total += gas.income

    for aksiz in aksizes:
        aksiz_total += aksiz.income

    for elektor in elektors:
        elektor_total += elektor.income

    for kredit in kredits:
        kredit_total += kredit.income

    for other in others:
        other_total += other.income

    for debt in debts:
        print(debt.debt)
        debt_total += debt.debt

    context = {
        "categories":category,
        "cattitle":categ,
        "main_income":main_income,
        "main_outcome":main_outcome,
        "income_total":income_total,
        "outcome_total":outcome_total,
        "gas_total":gas_total,
        "aksiz_total":aksiz_total,
        "elektor_total":elektor_total,
        "kredit_total":kredit_total,
        "other_total":other_total,
        "debt_total":debt_total,
    }

    return render(request, 'main_bill.html',context)


def main_reports_par(request):
    category = Filial.objects.all()
    for cat in category:
        if str(cat) in "Parfum distibyuter":
            categ = cat
    current_month = now().month
    main_income = Main_XR_income.objects.select_related('category').filter(category=categ,date__month=current_month)
    main_outcome = Main_XR_outcome.objects.select_related('category').filter(category=categ,date__month=current_month)
    gases = Xudud_XR_income.objects.select_related('category').filter(category=categ,date__month=current_month)
    aksizes = Aksiz_XR_income.objects.select_related('category').filter(category=categ,date__month=current_month)
    elektors = Elector_XR_income.objects.select_related('category').filter(category=categ,date__month=current_month)
    kredits = Credit_income.objects.select_related('category').filter(category=categ,date__month=current_month)
    debts = Debts.objects.select_related('category').filter(category=categ,date__month=current_month)
    others = Others.objects.select_related('category').filter(category=categ,date__month=current_month)
    income_total = 0
    outcome_total = 0
    gas_total = 0
    aksiz_total = 0
    elektor_total = 0
    kredit_total = 0
    other_total = 0
    debt_total = 0

    for y in main_income:
        income_total += y.income

    for y in main_outcome:
        outcome_total += y.outcome

    for gas in gases:
        gas_total += gas.income

    for aksiz in aksizes:
        aksiz_total += aksiz.income

    for elektor in elektors:
        elektor_total += elektor.income

    for kredit in kredits:
        kredit_total += kredit.income

    for other in others:
        other_total += other.income

    for debt in debts:
        print(debt.debt)
        debt_total += debt.debt

    context = {
        "categories":category,
        "cattitle":categ,
        "main_income":main_income,
        "main_outcome":main_outcome,
        "income_total":income_total,
        "outcome_total":outcome_total,
        "gas_total":gas_total,
        "aksiz_total":aksiz_total,
        "elektor_total":elektor_total,
        "kredit_total":kredit_total,
        "other_total":other_total,
        "debt_total":debt_total,
    }

    return render(request, 'main_bill.html',context)



def postDetail(request,p_id):
    post = Addmaingas.objects.select_related('category').get(id=p_id)
    naqt_sum = post.chec
    uzcard_sum = post.card_uz
    humocard_sum = post.card_humo
    today = datetime.today()
    naqt_tr = str(post.naqt)
    uz_tr = str(post.uzcard)
    humo_tr = str(post.humo)
    if request.method == "POST":
        form = Addbank(request.POST)
        f = form.save(commit=False)
        if f.naqt == True:
            post.naqt = True
            chec_sum = post.chec
            no_mon = post.no_money - post.chec
            post.no_money = no_mon
            have_mon_1 = post.have_money + post.chec
            post.have_money = have_mon_1
            main = Main_XR.objects.select_related('category').get(category = post.category,date=today)
            main_xr = main.bill + chec_sum
            main.bill = main_xr
            main_income = Main_XR_income.objects.create(category=post.category,income=chec_sum,description=f"{post.category} dan naqt")
            main_income.save()
            main.save()
            post.save()
        if f.uzcard == True:
            post.uzcard = True
            uz_sum = post.card_uz
            no_mon = post.no_money - post.card_uz
            post.no_money = no_mon
            have_mon_1 = post.have_money + post.card_uz
            post.have_money = have_mon_1
            main = Main_XR.objects.select_related('category').get(category = post.category,date=today)
            main_xr = main.bill + uz_sum
            main.bill = main_xr
            main_income = Main_XR_income.objects.create(category=post.category,income=uz_sum,description=f"{post.category} dan uzcard")
            main_income.save()
            main.save()
            post.save()
        if f.humo == True:
            post.humo = True
            hum_sum = post.card_humo
            no_mon = post.no_money - post.card_humo
            post.no_money = no_mon
            have_mon_1 = post.have_money + post.card_humo
            post.have_money = have_mon_1
            main = Main_XR.objects.select_related('category').get(category = post.category,date=today)
            main_xr = main.bill + hum_sum
            main.bill = main_xr
            main_income = Main_XR_income.objects.create(category=post.category,income=hum_sum,description=f"{post.category} dan humo")
            main_income.save()
            main.save()
            post.save()
        else:
            print("False")
        print(f.humo)
        return redirect('main:detail',p_id=post.id)
    else:
        form = Addbank()
        print("NOT " * 5)

    context = {
        "obj":post,
        "form":form,
        "naqt_tr":naqt_tr,
        "uz_tr":uz_tr,
        "humo_tr":humo_tr,
        "naqt_sum":naqt_sum,
        "uzcard_sum":uzcard_sum,
        "humocard_sum":humocard_sum,
    }

    return render(request, "detail.html", context)





def nasgasraports(request):
    category = Filial.objects.all()
    for cat in category:
        if str(cat) in "Nasirullo xoji":
            cate = cat
    current_month = now().month
    gases = Xududgaz_XR.objects.select_related('category').filter(category=cate,date__month=current_month)
    gas_income = Xudud_XR_income.objects.select_related('category').filter(category=cate,date__month=current_month)
    gas_outcome = Xudud_XR_outcome.objects.select_related('category').filter(category=cate,date__month=current_month)

    income_total = 0
    outcome_total = 0


    for incom in gas_income:
        income_total += incom.income


    for outcom in gas_outcome:
        outcome_total += outcom.outcome



    context = {
        "cattitle":cate,
        "categories":category,
        "gases":gases[::-1],
        "gas_income":gas_income,
        "gas_outcome":gas_outcome,
        "income_total":income_total,
        "outcome_total":outcome_total,
    }
    return render(request, "gasraports.html", context)



def sanoatgasraports(request):
    category = Filial.objects.all()
    for cat in category:
        if str(cat) in "Sanoat tranzit":
            cate = cat
    current_month = now().month
    gases = Xududgaz_XR.objects.select_related('category').filter(category=cate,date__month=current_month)
    gas_income = Xudud_XR_income.objects.select_related('category').filter(category=cate,date__month=current_month)
    gas_outcome = Xudud_XR_outcome.objects.select_related('category').filter(category=cate,date__month=current_month)


    income_total = 0
    outcome_total = 0


    for incom in gas_income:
        income_total += incom.income


    for outcom in gas_outcome:
        outcome_total += outcom.outcome



    context = {
        "cattitle":cate,
        "categories":category,
        "gases":gases[::-1],
        "gas_income":gas_income,
        "gas_outcome":gas_outcome,
        "income_total":income_total,
        "outcome_total":outcome_total,
    }
    return render(request, "gasraports.html", context)

def parfumgasraports(request):
    category = Filial.objects.all()
    for cat in category:
        if str(cat) in "Parfum distibyuter":
            cate = cat
    current_month = now().month
    gases = Xududgaz_XR.objects.select_related('category').filter(category=cate,date__month=current_month)
    gas_income = Xudud_XR_income.objects.select_related('category').filter(category=cate,date__month=current_month)
    gas_outcome = Xudud_XR_outcome.objects.select_related('category').filter(category=cate,date__month=current_month)

    income_total = 0
    outcome_total = 0


    for incom in gas_income:
        income_total += incom.income


    for outcom in gas_outcome:
        outcome_total += outcom.outcome



    context = {
        "cattitle":cate,
        "categories":category,
        "gases":gases[::-1],
        "gas_income":gas_income,
        "gas_outcome":gas_outcome,
        "income_total":income_total,
        "outcome_total":outcome_total,
    }
    return render(request, "gasraports.html", context)



def nasirulloaksizraports(request):
    category = Filial.objects.all()
    for cat in category:
        if str(cat) in "Nasirullo xoji":
            cate = cat
    current_month = now().month
    aksizes = Aksiz_XR.objects.select_related('category').filter(category=cate,date__month=current_month)
    aksiz_income = Aksiz_XR_income.objects.select_related('category').filter(category=cate,date__month=current_month)
    aksiz_outcome = Aksiz_XR_outcome.objects.select_related('category').filter(category=cate,date__month=current_month)

    income_total = 0
    outcome_total = 0


    for incom in aksiz_income:
        income_total += incom.income


    for outcom in aksiz_outcome:
        outcome_total += outcom.outcome



    context = {
        "cattitle":cate,
        "categories":category,
        "gases":aksizes[::-1],
        "gas_income":aksiz_income,
        "gas_outcome":aksiz_outcome,
        "income_total":income_total,
        "outcome_total":outcome_total,
    }
    return render(request, "akiszraports.html", context)





def sanoataksizraports(request):
    category = Filial.objects.all()
    for cat in category:
        if str(cat) in "Sanoat tranzit":
            cate = cat
    current_month = now().month
    aksizes = Aksiz_XR.objects.select_related('category').filter(category=cate,date__month=current_month)
    aksiz_income = Aksiz_XR_income.objects.select_related('category').filter(category=cate,date__month=current_month)
    aksiz_outcome = Aksiz_XR_outcome.objects.select_related('category').filter(category=cate,date__month=current_month)

    income_total = 0
    outcome_total = 0


    for incom in aksiz_income:
        income_total += incom.income


    for outcom in aksiz_outcome:
        outcome_total += outcom.outcome



    context = {
        "cattitle":cate,
        "categories":category,
        "gases":aksizes[::-1],
        "gas_income":aksiz_income,
        "gas_outcome":aksiz_outcome,
        "income_total":income_total,
        "outcome_total":outcome_total,
    }
    return render(request, "akiszraports.html", context)




def parfumaksizraports(request):
    category = Filial.objects.all()
    for cat in category:
        if str(cat) in "Parfum distibyuter":
            cate = cat
    current_month = now().month
    aksizes = Aksiz_XR.objects.select_related('category').filter(category=cate,date__month=current_month)
    aksiz_income = Aksiz_XR_income.objects.select_related('category').filter(category=cate,date__month=current_month)
    aksiz_outcome = Aksiz_XR_outcome.objects.select_related('category').filter(category=cate,date__month=current_month)

    income_total = 0
    outcome_total = 0


    for incom in aksiz_income:
        income_total += incom.income


    for outcom in aksiz_outcome:
        outcome_total += outcom.outcome



    context = {
        "cattitle":cate,
        "categories":category,
        "gases":aksizes[::-1],
        "gas_income":aksiz_income,
        "gas_outcome":aksiz_outcome,
        "income_total":income_total,
        "outcome_total":outcome_total,
    }
    return render(request, "akiszraports.html", context)




def nasirulloelectorraports(request):
    category = Filial.objects.all()
    for cat in category:
        if str(cat) in "Nasirullo xoji":
            cate = cat
    current_month = now().month
    electors = Elector_XR.objects.select_related('category').filter(category=cate,date__month=current_month)
    elector_income = Elector_XR_income.objects.select_related('category').filter(category=cate,date__month=current_month)
    elector_outcome = Elector_XR_outcome.objects.select_related('category').filter(category=cate,date__month=current_month)

    income_total = 0
    outcome_total = 0


    for incom in elector_income:
        income_total += incom.income


    for outcom in elector_outcome:
        outcome_total += outcom.outcome



    context = {
        "cattitle":cate,
        "categories":category,
        "electors":electors[::-1],
        "gas_income":elector_income,
        "gas_outcome":elector_outcome,
        "income_total":income_total,
        "outcome_total":outcome_total,
    }
    return render(request, "electorraports.html", context)





def sanoatelectorraports(request):
    category = Filial.objects.all()
    for cat in category:
        if str(cat) in "Sanoat tranzit":
            cate = cat
    current_month = now().month
    electors = Elector_XR.objects.select_related('category').filter(category=cate,date__month=current_month)
    elector_income = Elector_XR_income.objects.select_related('category').filter(category=cate,date__month=current_month)
    elector_outcome = Elector_XR_outcome.objects.select_related('category').filter(category=cate,date__month=current_month)

    income_total = 0
    outcome_total = 0


    for incom in elector_income:
        income_total += incom.income


    for outcom in elector_outcome:
        outcome_total += outcom.outcome



    context = {
        "cattitle":cate,
        "categories":category,
        "electors":electors[::-1],
        "gas_income":elector_income,
        "gas_outcome":elector_outcome,
        "income_total":income_total,
        "outcome_total":outcome_total,
    }
    return render(request, "electorraports.html", context)



def parfumelelectorraports(request):
    category = Filial.objects.all()
    for cat in category:
        if str(cat) in "Parfum distibyuter":
            cate = cat
    current_month = now().month
    electors = Elector_XR.objects.select_related('category').filter(category=cate,date__month=current_month)
    elector_income = Elector_XR_income.objects.select_related('category').filter(category=cate,date__month=current_month)
    elector_outcome = Elector_XR_outcome.objects.select_related('category').filter(category=cate,date__month=current_month)

    income_total = 0
    outcome_total = 0


    for incom in elector_income:
        income_total += incom.income


    for outcom in elector_outcome:
        outcome_total += outcom.outcome



    context = {
        "cattitle":cate,
        "categories":category,
        "electors":electors[::-1],
        "gas_income":elector_income,
        "gas_outcome":elector_outcome,
        "income_total":income_total,
        "outcome_total":outcome_total,
    }
    return render(request, "electorraports.html", context)












def get_previous_month_date_range():
    today = datetime.today()
    first_day_of_current_month = today.replace(day=1)
    last_day_of_previous_month = first_day_of_current_month - timedelta(days=1)
    first_day_of_previous_month = last_day_of_previous_month.replace(day=1)
    
    return first_day_of_previous_month, last_day_of_previous_month

def all_sale_gas_nas(request):
    if request.user.is_staff:
        category = Filial.objects.all()
        for cat in category:
            if str(cat) in "Nasirullo xoji":
                category_name = cat
                print(category_name)
        current_month = now().month
        obj = Addmaingas.objects.select_related('category').filter(category=category_name,date__month=current_month)
        start_date, end_date = get_previous_month_date_range()
        previous_month_data = Addmaingas.objects.select_related('category').filter(category=category_name,date__gte=start_date, date__lte=end_date)


        context = {
            "categories":category,
            "category_name":category_name,
            "object":obj,
            "previous_month_data":previous_month_data,

            
        } 

        return render(request, "all_sale_gas_1.html", context)



def all_sale_gas_san(request):
    if request.user.is_staff:
        category = Filial.objects.all()
        for cat in category:
            if str(cat) in "Sanoat tranzit":
                category_name = cat
                print(category_name)
        current_month = now().month
        obj = Addmaingas.objects.select_related('category').filter(category=category_name,date__month=current_month)
        start_date, end_date = get_previous_month_date_range()
        previous_month_data = Addmaingas.objects.select_related('category').filter(category=category_name,date__gte=start_date, date__lte=end_date)

        context = {
            "categories":category,
            "category_name":category_name,
            "object":obj,
            "previous_month_data":previous_month_data,
            
        } 

        return render(request, "all_sale_gas_1.html", context)


def all_sale_gas_par(request):
    if request.user.is_staff:
        category = Filial.objects.all()
        for cat in category:
            if str(cat) in "Parfum distibyuter":
                category_name = cat
                print(category_name)
        current_month = now().month
        obj = Addmaingas.objects.select_related('category').filter(category=category_name,date__month=current_month)
        start_date, end_date = get_previous_month_date_range()
        previous_month_data = Addmaingas.objects.select_related('category').filter(category=category_name,date__gte=start_date, date__lte=end_date)

        for x in obj:
            total_sum += x.buy_sum
        context = {
            "categories":category,
            "category_name":category_name,
            "object":obj,
            "previous_month_data":previous_month_data,
            
        } 

        return render(request, "all_sale_gas_1.html", context)





def category_list(request, category_slug):
    main_today = 0
    other_today = 0
    
    total_gas = 0
    total_aksiz = 0
    total_elek = 0
    total_buy_gas = 0
    total_sale_gas = 0
    total_tash = 0
    total_card = 0
    total_check = 0
    total_savdo = 0
    total_tushgan = 0
    total_tushmagan = 0
    total_profit = 0
    obj = Filial.objects.all()
    category = Filial.objects.get(slug=category_slug)
    current_month = now().month



    date = request.GET.get('date', None)
        

    if date:
        date_date = date
        reports = Addmaingas.objects.select_related('category').filter(category=category,date=date)
        stations = Manag_totals.objects.select_related('category').filter(category=category,date=date)
        main_xr = Main_XR.objects.select_related('category').get(category=category,date=date)
        xudud_xr = Xududgaz_XR.objects.select_related('category').get(category=category,date=date)
        aksiz_xr = Aksiz_XR.objects.select_related('category').get(category=category,date=date)
        elector = Elector_XR.objects.select_related('category').get(category=category,date=date)
        company = Company_XR.objects.select_related('category').get(category=category,date=date)
        cardit = Credit.objects.select_related('category').get(category=category,date=date)
        out_main = Main_XR_outcome.objects.select_related('category').filter(category=category,date=date)
        out_xudud = Xudud_XR_outcome.objects.select_related('category').filter(category=category,date=date)
        out_aksiz = Aksiz_XR_outcome.objects.select_related('category').filter(category=category,date=date)
        out_elec = Elector_XR_outcome.objects.select_related('category').filter(category=category,date=date)
        out_company = Company_XR_income.objects.select_related('category').filter(category=category,date=date)
        out_credit = Credit_income.objects.select_related('category').filter(category=category,date=date)
        others = Others.objects.select_related('category').filter(category=category,date=date)
        category_name = str(category_slug.capitalize())
    else:
        date_date_2 = datetime.today()
        date_date = date_date_2.strftime('%Y-%m-%d')
        reports = Addmaingas.objects.select_related('category').filter(category=category)
        stations = Manag_totals.objects.select_related('category').filter(category=category)
        main_xr = Main_XR.objects.select_related('category').get(category=category,date=datetime.today())
        xudud_xr = Xududgaz_XR.objects.select_related('category').get(category=category,date=datetime.today())
        aksiz_xr = Aksiz_XR.objects.select_related('category').get(category=category,date=datetime.today())
        elector = Elector_XR.objects.select_related('category').get(category=category,date=datetime.today())
        company = Company_XR.objects.select_related('category').get(category=category,date=datetime.today())
        cardit = Credit.objects.select_related('category').get(category=category,date=datetime.today())
        out_main = Main_XR_outcome.objects.select_related('category').filter(category=category,date=datetime.today())
        out_xudud = Xudud_XR_outcome.objects.select_related('category').filter(category=category,date=datetime.today())
        out_aksiz = Aksiz_XR_outcome.objects.select_related('category').filter(category=category,date=datetime.today())
        out_elec = Elector_XR_outcome.objects.select_related('category').filter(category=category,date=datetime.today())
        out_company = Company_XR_income.objects.select_related('category').filter(category=category,date=datetime.today())
        out_credit = Credit_income.objects.select_related('category').filter(category=category,date=datetime.today())
        others = Others.objects.select_related('category').filter(category=category,date=datetime.today())
        category_name = str(category_slug.capitalize())


    for totals in reports:
        total_gas += totals.last_gas
        total_aksiz += totals.aksiz_sum
        total_elek += totals.elec_sum
        total_buy_gas += totals.buy_sum
        total_sale_gas += totals.total_sum
        total_tash += totals.company
        total_card += totals.card
        total_check += totals.chec
        total_savdo += totals.sum_half
        total_tushgan += totals.have_money
        total_tushmagan += totals.no_money
        total_profit += totals.profit


    # print(total_gas, "gaz")
    # print(total_aksiz, "aksiz")
    # print(total_elek, "elektor")
    # print(total_buy_gas, "sotibolgan")
    # print(total_sale_gas, "sotilgan")
    # print(total_tash, "tashkilot")
    # print(total_card, "karta")
    # print(total_check, "naqt")
    # print(total_savdo, "savdo")
    # print(total_tushgan, "tushgan")
    # print(total_tushmagan, "tushmagan")
    # print(total_profit, "foyda")
    


    for main in out_main:
        main_today += main.outcome

    for other in others:
        other_today += other.income


    yesterday_before = datetime.now() - timedelta(days=2)
    total_buy_gases_yes = Addmaingas.objects.select_related('category').filter(date=yesterday_before)
        
    add = 0

    for x in total_buy_gases_yes:
        cat = x.category
        
        if str(cat) in "Nasirullo xoji":
            add += 1
        if str(cat) in "Sanoat tranzit":
            add += 1
        if str(cat) in "Parfum distibyuter":
            add += 1

    print(add)

    context = {
        "add":add,
        "date_date":date_date,
        "object_list":reports,
        "stations":stations,
        "categories":obj,
        'category_name': category_name,
        "main_xr":main_xr,
        "xudud_xr":xudud_xr,
        "aksiz_xr":aksiz_xr,
        "company":company,
        "elector":elector,
        "cardit":cardit,
        "out_main":main_today,
        "out_xudud":out_xudud,
        "out_aksiz":out_aksiz,
        "out_company":out_company,
        "others":others,
        "other_today":other_today,
        "out_credit":out_credit,
        "out_elec":out_elec,
        "total_gas":total_gas,
        "total_aksiz":total_aksiz,
        "total_elek":total_elek,
        "total_buy_gas":total_buy_gas,
        "total_sale_gas":total_sale_gas,
        "total_tash":total_tash,
        "total_card":total_card,
        "total_check":total_check,
        "total_savdo":total_savdo,
        "total_tushgan":total_tushgan,
        "total_tushmagan":total_tushmagan,
        "total_profit":total_profit,
        }
    return render(request, "cat.html", context)



def addmaingas(request):
    sale_sum = Saleprice.objects.get()
    lose_nas = Nasrullo_lose.objects.get()
    lose_san = Sanoat_lose.objects.get()
    lose_par = Parfum_lose.objects.get()
    obj = Filial.objects.all()
    buy = Buyprice.objects.get()
    aksiz_tax = Aksiz.objects.get()
    elek_tax = Elector.objects.get()
    today = datetime.today()
    yesterday = datetime.now() - timedelta(days=1)
    yesterday_1 = yesterday.strftime('%Y-%m-%d')
    if request.user.is_staff:
        if request.method == "POST":
            form = AddMainGasForm(request.POST)
            if form.is_valid():
                f = form.save(commit=False)
                cat = f.category
                station_gas = Manag_totals.objects.select_related('category').filter(category=cat)
                for gas in station_gas:
                    if str(gas.date) in str(yesterday_1):
                        # print("Bor davay")
                        gases = Addmaingas.objects.select_related('category').filter(category=cat)
                        for fil in gases:
                            if str(fil.date) in str(yesterday_1):
                                message_1 = "Ma'lumot qo'shilgan"
                                message_2 = "Iltimos ma'lumotlaringizni tekshiring"
                                context = {
                                    "message_1":message_1,
                                    "message_2":message_2,
                                }
                                return render(request, "add_gas_error.html", context)
                            else:
                                f.author = request.user
                                gas_main_remain = f.last_gas
                                f.sale_price = sale_sum.saleprice
                                station = Manag_totals.objects.select_related('category').get(category = cat, date=yesterday)

                                
                                f.buygasprice = buy.buyprice
                                all_sum_buy = gas_main_remain * buy.buyprice
                                f.buy_sum = all_sum_buy
                                xudud_xr = Xududgaz_XR.objects.select_related('category').get(category=cat,date=today)
                                xudud_xr_add = xudud_xr.bill
                                xudud_add = xudud_xr_add - all_sum_buy
                                xudud_xr.bill = xudud_add
                                xudud_xr.save()

                                xudud_xr_outcome = Xudud_XR_outcome.objects.create(category=cat,outcome = all_sum_buy)
                                xudud_xr_outcome.save()

                                f.elector = elek_tax.elector
                                all_sum_elek = gas_main_remain * elek_tax.elector
                                f.elec_sum = all_sum_elek
                                elek_xr = Elector_XR.objects.get(category=cat,date=today)
                                elek_xr_add = elek_xr.bill
                                elek_add = elek_xr_add - all_sum_elek
                                elek_xr.bill = elek_add
                                elek_xr.save()

                                elek_xr_outcome = Elector_XR_outcome.objects.create(category=cat,outcome = all_sum_elek)
                                elek_xr_outcome.save()

                                
                                f.aksiz = aksiz_tax.aksiz
                                lose_gas = gas_main_remain / 100
                                if str(cat) == "Nasirullo xoji":
                                    lose_gas_2 = lose_gas * lose_nas.losegas
                                    f.lose_gas = lose_gas_2
                                if str(cat) == "Sanoat tranzit":
                                    lose_gas_2 = lose_gas * lose_san.losegas
                                    f.lose_gas = lose_gas_2
                                if str(cat) == "Parfum distibyuter":
                                    lose_gas_2 = lose_gas * lose_par.losegas
                                    f.lose_gas = lose_gas_2
                                lose_gas_3 = gas_main_remain - lose_gas_2
                                f.remain_gas = lose_gas_3
                                print(lose_gas_3)
                                all_sum_aksiz = lose_gas_3 * aksiz_tax.aksiz
                                f.aksiz_sum = all_sum_aksiz
                                aksiz_xr = Aksiz_XR.objects.select_related('category').get(category=cat,date=today)
                                aksiz_xr_add = aksiz_xr.bill
                                aksiz_add = aksiz_xr_add - all_sum_aksiz
                                aksiz_xr.bill = aksiz_add
                                aksiz_xr.save()

                                aksiz_xr_outcome = Aksiz_XR_outcome.objects.create(category=cat,outcome = all_sum_aksiz)
                                aksiz_xr_outcome.save()



                                sum_half = lose_gas_3 * sale_sum.saleprice
                                print(sum_half)
                                f.total_sum = sum_half
                                f.card = station.card
                                chec_1 =  sum_half - station.company
                                f.chec = chec_1 - station.card
                                f.card_uz = station.card_uz
                                f.card_humo = station.card_humo
                                f.company = station.company
                                company = Company_XR.objects.select_related('category').get(category=cat,date=today)
                                minus_xr = company.bill
                                company_minus = minus_xr + f.company
                                company.bill = company_minus
                                company.save()

                                company_income = Company_XR_income.objects.create(category=cat,income=f.company,date=today)
                                company_income.save()
                                out_com = sum_half - station.company
                                f.sum_half = out_com
                                f.no_money = out_com
                                profit = sum_half - all_sum_buy
                                profit_1 = profit - all_sum_aksiz
                                profit_2 = profit_1 - all_sum_elek
                                f.profit = profit_2
                                f.date = yesterday
                                f.save()

                                if str(cat) == "Nasirullo xoji":
                                    return redirect('/nasirullo-xoji/category/')
                                if str(cat) == "Sanoat tranzit":
                                    return redirect('/sanoat-tranzit/category/')
                                if str(cat) == "Parfum distibyuter":
                                    return redirect('/parfum-distibyuter/category/')
                    else:
                        print("Yo'q") 
                        message_1 = "Malumot kirita olmaysiz!"
                        message_2 = f"{cat} zaprafkaning kechagi kungi ma'lumoti kiritlmagan \n  Iltimos ma'lumotni kiritishini kuting yoki \n ma'lumot kiritish kerakligini habarini berin"
                        context = {
                            "message_1":message_1,
                            "message_2":message_2,
                        }
                        return render(request, "add_gas_error.html", context)

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
       


def addmaingasyes(request):
    sale_sum = Saleprice.objects.get()
    lose_nas = Nasrullo_lose.objects.get()
    lose_san = Sanoat_lose.objects.get()
    lose_par = Parfum_lose.objects.get()
    obj = Filial.objects.all()
    buy = Buyprice.objects.get()
    aksiz_tax = Aksiz.objects.get()
    elek_tax = Elector.objects.get()
    yesterday = datetime.now() - timedelta(days=1)
    yesterday_befor = datetime.now() - timedelta(days=2)
    yesterday_befor_1 = yesterday_befor.strftime('%Y-%m-%d')
    if request.user.is_staff:
        if request.method == "POST":
            form = AddMainGasForm(request.POST)
            if form.is_valid():
                f = form.save(commit=False)
                cat = f.category
                station_gas = Manag_totals.objects.select_related('category').filter(category=cat)
                for gas in station_gas:
                    if str(gas.date) in str(yesterday_befor_1):
                        # print("Bor davay")
                        gases = Addmaingas.objects.select_related('category').filter(category=cat)
                        for fil in gases:
                            if str(fil.date) in str(yesterday_befor_1):
                                message_1 = "Ma'lumot qo'shilgan"
                                message_2 = "Iltimos ma'lumotlaringizni tekshiring"
                                context = {
                                    "message_1":message_1,
                                    "message_2":message_2,
                                }
                                return render(request, "add_gas_error.html", context)
                            else:
                                f.author = request.user
                                gas_main_remain = f.last_gas
                                f.sale_price = sale_sum.saleprice
                                station = Manag_totals.objects.select_related('category').get(category = cat, date=yesterday_befor_1)

                                
                                f.buygasprice = buy.buyprice
                                all_sum_buy = gas_main_remain * buy.buyprice
                                f.buy_sum = all_sum_buy
                                xudud_xr = Xududgaz_XR.objects.select_related('category').get(category=cat,date=yesterday)
                                xudud_xr_add = xudud_xr.bill
                                xudud_add = xudud_xr_add - all_sum_buy
                                xudud_xr.bill = xudud_add
                                xudud_xr.save()

                                xudud_xr_outcome = Xudud_XR_outcome.objects.create(category=cat,outcome = all_sum_buy)
                                xudud_xr_outcome.save()

                                f.elector = elek_tax.elector
                                all_sum_elek = gas_main_remain * elek_tax.elector
                                f.elec_sum = all_sum_elek
                                elek_xr = Elector_XR.objects.select_related('category').get(category=cat,date=yesterday)
                                elek_xr_add = elek_xr.bill
                                elek_add = elek_xr_add - all_sum_elek
                                elek_xr.bill = elek_add
                                elek_xr.save()

                                elek_xr_outcome = Elector_XR_outcome.objects.create(category=cat,outcome = all_sum_elek)
                                elek_xr_outcome.save()

                                
                                f.aksiz = aksiz_tax.aksiz
                                lose_gas = gas_main_remain / 100
                                if str(cat) == "Nasirullo xoji":
                                    lose_gas_2 = lose_gas * lose_nas.losegas
                                    f.lose_gas = lose_gas_2
                                if str(cat) == "Sanoat tranzit":
                                    lose_gas_2 = lose_gas * lose_san.losegas
                                    f.lose_gas = lose_gas_2
                                if str(cat) == "Parfum distibyuter":
                                    lose_gas_2 = lose_gas * lose_par.losegas
                                    f.lose_gas = lose_gas_2
                                lose_gas_3 = gas_main_remain - lose_gas_2
                                f.remain_gas = lose_gas_3
                                print(lose_gas_3)
                                all_sum_aksiz = lose_gas_3 * aksiz_tax.aksiz
                                f.aksiz_sum = all_sum_aksiz
                                aksiz_xr = Aksiz_XR.objects.get(category=cat,date=yesterday)
                                aksiz_xr_add = aksiz_xr.bill
                                aksiz_add = aksiz_xr_add - all_sum_aksiz
                                aksiz_xr.bill = aksiz_add
                                aksiz_xr.save()

                                aksiz_xr_outcome = Aksiz_XR_outcome.objects.create(category=cat,outcome = all_sum_aksiz)
                                aksiz_xr_outcome.save()



                                sum_half = lose_gas_3 * sale_sum.saleprice
                                print(sum_half)
                                f.total_sum = sum_half
                                f.card = station.card
                                chec_1 =  sum_half - station.company
                                f.chec = chec_1 - station.card
                                f.card_uz = station.card_uz
                                f.card_humo = station.card_humo
                                f.company = station.company
                                company = Company_XR.objects.select_related('category').get(category=cat,date=yesterday)
                                minus_xr = company.bill
                                company_minus = minus_xr + f.company
                                company.bill = company_minus
                                company.save()

                                company_income = Company_XR_income.objects.create(category=cat,income=f.company,date=yesterday)
                                company_income.save()
                                out_com = sum_half - station.company
                                f.sum_half = out_com
                                f.no_money = out_com
                                profit = sum_half - all_sum_buy
                                profit_1 = profit - all_sum_aksiz
                                profit_2 = profit_1 - all_sum_elek
                                f.profit = profit_2
                                f.date = yesterday_befor
                                f.save()

                                if str(cat) == "Nasirullo xoji":
                                    return redirect('/nasirullo-xoji/category/')
                                if str(cat) == "Sanoat tranzit":
                                    return redirect('/sanoat-tranzit/category/')
                                if str(cat) == "Parfum distibyuter":
                                    return redirect('/parfum-distibyuter/category/')
                    else:
                        print("Yo'q") 
                        message_1 = "Malumot kirita olmaysiz!"
                        message_2 = f"{cat} zaprafkaning {yesterday_befor_1} kungi ma'lumoti kiritlmagan \n  Iltimos ma'lumotni kiritishini kuting yoki \n ma'lumot kiritish kerakligini habarini berin"
                        context = {
                            "message_1":message_1,
                            "message_2":message_2,
                        }
                        return render(request, "add_gas_error.html", context)

        else:
            form = AddMainGasForm()
            print("NOT " * 5)
        
        context = {
            "for":form,
            "categories":obj,
            }
        return render(request, "add_to_gas_yes.html",context)

    else:
        return redirect('/')


def additionalmoney(request):
    obj = Filial.objects.all()
    today = datetime.today()
    if request.user.is_staff:
        if request.method == "POST":
            form = AdditionalmoneyForm(request.POST)
            if form.is_valid():
                f = form.save(commit=False)
                cat = f.category
                main = Main_XR.objects.select_related('category').get(category=cat,date=today)
                print(f.income)
                print(main.bill)
                main_add = main.bill + f.income
                main.bill = main_add
                main.save()
                print(main_add)
                print(f.category)
                print(f.description)
                f.save()
                if str(cat) == "Nasirullo xoji":
                    return redirect('/nasirullo-xoji/category/')
                if str(cat) == "Sanoat tranzit":
                    return redirect('/sanoat-tranzit/category/')
                if str(cat) == "Parfum distibyuter":
                    return redirect('/parfum-distibyuter/category/')
        else:
            form = AdditionalmoneyForm()
            print("NOT " * 5)
        
        context = {
            "for":form,
            "categories":obj
        }
        return render(request, "additional_money.html", context)
    else:
        return redirect('/')




def get_money(request):
    obj = Filial.objects.all()
    today = datetime.today()
    if request.user.is_staff:
        if request.method == "POST":
            form = GetMoneyeachForm(request.POST)
            if form.is_valid():
                f = form.save(commit=False)
                lend_money = Main_XR.objects.select_related('category').get(category=f.bring_money,date=today)
                print(lend_money.bill,f.bring_money,lend_money.category)
                lend = lend_money.bill - f.bill
                lend_money.bill = lend
                print(f.bill)
                print(lend_money.bill)
                lend_money.save()

                lend_out = Main_XR_outcome.objects.create(category=f.bring_money,outcome = f.bill,description = f"{f.get_money} ga qarz",date=today)
                lend_out.save()

                debt = Debts.objects.create(category=f.bring_money,debt = f.bill,date=today)
                debt.save()

                get_money = Main_XR.objects.select_related('category').get(category=f.get_money,date=today)
                print(get_money.bill,f.get_money,get_money.category)

                get = get_money.bill + f.bill
                get_money.bill = get
                print(f.bill)
                print(get_money.bill)
                get_money.save()

                get_in = Main_XR_income.objects.select_related('category').create(category=f.get_money,income = f.bill,description = f"{f.bring_money} dan qarz",date=today)
                get_in.save()

                f.date = today
                print(f.date)
                if str(f.get_money) == "Nasirullo xoji":
                    return redirect('/nasirullo-xoji/category/')
                if str(f.get_money) == "Sanoat tranzit":
                    return redirect('/sanoat-tranzit/category/')
                if str(f.get_money) == "Parfum distibyuter":
                    return redirect('/parfum-distibyuter/category/')
        else:
            form = GetMoneyeachForm()
            print("NOT " * 5)
        
        context = {
            "for":form,
            "categories":obj
        }

        return render(request, "borrow_money.html", context)

    else:
        return redirect('/')



def addincome(request):
    obj = Filial.objects.all()
    send = Send.objects.get()
    today = datetime.today()
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
                    main_xr = Main_XR.objects.select_related('category').get(category=cat,date=today)
                    minus_xr = main_xr.bill
                    tax = sum / 100
                    tax_1 = tax * send_tax
                    tax_2 = sum + tax_1
                    main_minus = minus_xr - tax_2
                    main_xr.bill = main_minus
                    main_xr.save()
                    main_outcome = Main_XR_outcome.objects.create(category=cat,outcome = tax_2,description=f.description,date=today)
                    main_outcome.save()


                    xudud_xr = Xududgaz_XR.objects.select_related('category').get(category=cat,date=today)
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
                    main_xr = Main_XR.objects.select_related('category').get(category=cat,date=today)
                    minus_xr = main_xr.bill
                    tax = sum / 100
                    tax_1 = tax * send_tax
                    tax_2 = sum + tax_1
                    main_minus = minus_xr - tax_2
                    main_xr.bill = main_minus
                    main_xr.save()
                    main_outcome = Main_XR_outcome.objects.create(category=cat,outcome = tax_2,description=f.description,date=today)
                    main_outcome.save()

                
                    aksiz_xr = Aksiz_XR.objects.select_related('category').get(category=cat,date=today)
                    aksiz_xr_add = aksiz_xr.bill
                    aksiz_add = aksiz_xr_add + sum
                    aksiz_xr.bill = aksiz_add
                    aksiz_xr.save()

                    aksiz_xr_income = Aksiz_XR_income.objects.create(category=cat,income = sum)
                    aksiz_xr_income.save()
                else: 
                    print("Aksiz ga qo'shilmadi")

                if str(f.income) == 'Elektro svet':
                    print("Elektro svetga qo'shilda")

                    send_tax = send.send_tax
                    main_xr = Main_XR.objects.select_related('category').get(category=cat,date=today)
                    minus_xr = main_xr.bill
                    tax = sum / 100
                    tax_1 = tax * send_tax
                    tax_2 = sum + tax_1
                    main_minus = minus_xr - tax_2
                    main_xr.bill = main_minus
                    main_xr.save()
                    main_outcome = Main_XR_outcome.objects.create(category=cat,outcome = tax_2,description=f.description,date=today)
                    main_outcome.save()


                    elec_xr = Elector_XR.objects.select_related('category').get(category=cat,date=today)
                    elec_xr_add = elec_xr.bill
                    elec_add = elec_xr_add + sum
                    elec_xr.bill = elec_add
                    elec_xr.save()

                    elec_xr_income = Elector_XR_income.objects.create(category=cat,income = sum,date=today)
                    elec_xr_income.save()
                else:
                    print("Elektor ga qo'shilmadi")


                if str(f.income) == 'Boshqalar':
                    print("Boshqalar ga qo'shilda")
                    send_tax = send.send_tax
                    main_xr = Main_XR.objects.select_related('category').get(category=cat,date=today)
                    minus_xr = main_xr.bill
                    tax = sum / 100
                    tax_1 = tax * send_tax
                    tax_2 = sum + tax_1
                    main_minus = minus_xr - tax_2
                    main_xr.bill = main_minus
                    main_xr.save()
                    main_outcome = Main_XR_outcome.objects.create(category=cat,outcome = tax_2,description=f.description,date=today)
                    main_outcome.save()

                    others_income = Others.objects.create(category=cat,income = sum,description=f.description,date=today)
                    others_income.save()
                else:
                    print("Boshqalar ga qo'shilmadi")
                f.save()

                if str(cat) == "Nasirullo xoji":
                    return redirect('/nasirullo-xoji/category/')
                if str(cat) == "Sanoat tranzit":
                    return redirect('/sanoat-tranzit/category/')
                if str(cat) == "Parfum distibyuter":
                    return redirect('/parfum-distibyuter/category/')
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



def pay_credit(request):
    obj = Filial.objects.all()
    today = datetime.today()
    send = Send.objects.get()
    if request.user.is_staff:
        if request.method == "POST":
            form = CareditPayForm(request.POST)
            if form.is_valid():
                f = form.save(commit=False)
                cat = f.category
                print(cat)
                print(f.dollar)
                print(f.income)
                sum = f.income
                send_tax = send.send_tax
                main_xr = Main_XR.objects.select_related('category').get(category=cat,date=today)
                minus_xr = main_xr.bill
                tax = sum / 100
                tax_1 = tax * send_tax
                tax_2 = sum + tax_1
                main_minus = minus_xr - tax_2
                main_xr.bill = main_minus
                main_xr.save()
                main_outcome = Main_XR_outcome.objects.create(category=cat,outcome = tax_2,description="Kredit uchun to'lov",date=today)
                main_outcome.save()


                credit_xr = Credit.objects.select_related('category').get(category=cat,date=today)
                credit_xr_add = credit_xr.bill
                credit_add = credit_xr_add - f.dollar
                credit_xr.bill = credit_add
                credit_xr.save()

                f.date = today
                print(f.date)
                f.save()
                if str(cat) == "Nasirullo xoji":
                    return redirect('/nasirullo-xoji/category/')
                if str(cat) == "Sanoat tranzit":
                    return redirect('/sanoat-tranzit/category/')
                if str(cat) == "Parfum distibyuter":
                    return redirect('/parfum-distibyuter/category/')
        else:
            form = CareditPayForm()
            print("NOT " * 5)
        
        context = {
            "for":form,
            "categories":obj
        }

        return render(request, "pay_kredit.html", context)

    else:
        return redirect('/')


def station_add_gas(request):
    yesterday = datetime.now() - timedelta(days=1)
    yesterday_before = datetime.now() - timedelta(days=2)
    yesterday_1 = yesterday.strftime('%Y-%m-%d')
    lose_nas = Nasrullo_lose.objects.get()
    lose_san = Sanoat_lose.objects.get()
    lose_par = Parfum_lose.objects.get()
    sale_sum = Saleprice.objects.get()
    number = request.user.number
    number_2 = str(number)
    category = Filial.objects.get(id=number_2)
    obj = Manag_totals.objects.select_related('category').filter(category=category)
    for fil in obj:
        if str(fil.date) in str(yesterday_1):
            message_1 = "Ma'lumot qo'shilgan"
            message_2 = "Iltimos ma'lumotlaringizni tekshiring"

            context = {
                "message_1":message_1,
                "message_2":message_2,
            }
            return render(request, "add_gas_error.html", context)
        else:
            user = request.user
            remain_gas = Manag_totals.objects.select_related('category').get(user=user,date=yesterday_before)
            if request.user.username == 'Sanoat tranzit':
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
                    
                        
                        y = int(remain_gas.counter)
                        
                        if y >= x_7:
                            print("Xisoblagich kichi",y)
                            message_1 = "Ma'lumot kiritishda hatolik"
                            message_2 = "Kiritgan ma'lumotingiz kechagi kun bilan to'g'ri kelmadi \n Ilrimos ma'lumotingizni qaytadan kiriting!"

                            context = {
                                "message_1":message_1,
                                "message_2":message_2,
                            }
                            return render(request, "add_gas_error.html", context)
                        else:
                            print("Xisoblagich katta",y)

                            remain_gas_1 = x_7 - y
                            f.remain_gas = remain_gas_1

                            lose_gas_1 = remain_gas_1 / 100
                            
                            lose_gas_2 = lose_gas_1 * lose_san.losegas

                            f.lose_gas = lose_gas_2

                            lose_end = remain_gas_1 - lose_gas_2
                            f.gas = lose_end
                            f.date = yesterday
                            total_sum = lose_end * sale_sum.saleprice
                            f.total_sum = total_sum
                            f.save()

                    return redirect('main:add_card_income')
                
                else:
                    form = Stationsalegas_8()
                    print("NOT " * 5)
                
                context = {
                    "form":form,
                }

                return render(request, "add_station_gas.html", context)

            if request.user.username == 'Nasirullo xoji':
                number = request.user.number
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
                        
                        y = int(remain_gas.counter)

                        if y > x_5:
                            print("Xisoblagich kichi",y)
                            message_1 = "Ma'lumot kiritishda hatolik"
                            message_2 = "Kiritgan ma'lumotingiz kechagi kun bilan to'g'ri kelmadi \n Ilrimos ma'lumotingizni qaytadan kiriting!"

                            context = {
                                "message_1":message_1,
                                "message_2":message_2,
                            }
                            return render(request, "add_gas_error.html", context)
                        else:
                            print("Xisoblagich katta",y)
                            remain_gas_1 = x_5 - y
                            f.remain_gas = remain_gas_1

                            lose_gas_1 = remain_gas_1 / 100
                            lose_gas_2 = lose_gas_1 * lose_nas.losegas
                            f.lose_gas = lose_gas_2
                            

                            lose_end = remain_gas_1 - lose_gas_2
                            f.gas = lose_end
                            f.date = yesterday
                            total_sum = lose_end * sale_sum.saleprice
                            f.total_sum = total_sum 

                            f.save()

                    return redirect('main:add_card_income')
                
                else:
                    form = Stationsalegas_6()
                    print("NOT " * 5)
                
                context = {
                    "form":form,
                }

                return render(request, "add_station_gas.html", context)
            
            if request.user.username == 'Parfum distibyuter':
                number = request.user.number
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

                        
                        y = int(remain_gas.counter)
                        
                        if y > x_5:
                            print("Xisoblagich kichi",y)
                            message_1 = "Ma'lumot kiritishda hatolik"
                            message_2 = "Kiritgan ma'lumotingiz kechagi kun bilan to'g'ri kelmadi \n Ilrimos ma'lumotingizni qaytadan kiriting!"

                            context = {
                                "message_1":message_1,
                                "message_2":message_2,
                            }
                            return render(request, "add_gas_error.html", context)
                        else:
                            print("Xisoblagich katta",y)
                            remain_gas_1 = x_5 - y
                            f.remain_gas = remain_gas_1

                            lose_gas_1 = remain_gas_1 / 100
                            lose_gas_2 = lose_gas_1 * lose_par.losegas
                            f.lose_gas = lose_gas_2

                            lose_end = remain_gas_1 - lose_gas_2
                            f.gas = lose_end
                            f.date = yesterday
                            total_sum = lose_end * sale_sum.saleprice
                            f.total_sum = total_sum
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
    yesterday = datetime.now() - timedelta(days=1)
    yesterday_1 = yesterday.strftime('%Y-%m-%d')
    sale = Saleprice.objects.get()
    user = request.user
    asd = Manag_add_gas.objects.select_related('category').filter(user=user)
    totals = Manag_add_gas.objects.select_related('category').filter(user=user,date = yesterday_1)
    gasyes = Manag_totals.objects.select_related('category').filter(user=user)
    user = request.user
    if request.user.is_authenticated:
        for no in gasyes:
            if str(no.date) not in str(yesterday_1):
                # print(no.date)
                for x in asd:
                    # print(x.gas)
                    if str(x.date) in str(yesterday_1):
                        # print("Bor")
                        # print(x.date)
                        if request.method == "POST":
                            form = Stationaddgas(request.POST)
                            if form.is_valid():
                                f = form.save(commit=False)
                                f.user = user

                                carduz = f.card_uz * sale.saleprice
                                f.card_uz = carduz

                                cardhumo = f.card_humo * sale.saleprice
                                f.card_humo = cardhumo

                                total_card = carduz + cardhumo
                                f.card = total_card

                                total_com = f.company * sale.saleprice
                                f.company = total_com
                                

                                for total in totals:
                                    f.category = total.category
                                    
                                f.counter = total.total_gas
                                f.total_gas = total.remain_gas
                                f.lose_gas = total.lose_gas
                                f.gas = total.gas
                                f.total_sum = total.total_sum
                                f.sale_price = sale.saleprice
                                sum_half = total.total_sum - f.company
                                f.sum_half = sum_half
                                check = sum_half - f.card
                                f.chec = check
                    
                                yesterday = datetime.now() - timedelta(days=1)
                                f.date = yesterday
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
                        # print("Yo'q")
                        return redirect('main:station_add_gas')
            else:
                # print("Bor")
                message_1 = "Ma'lumot qo'shilgan"
                message_2 = "Iltimos ma'lumotlaringizni tekshiring"

                context = {
                    "message_1":message_1,
                    "message_2":message_2,
                }
                return render(request, "add_gas_error.html", context)
    else:
        return redirect('/')