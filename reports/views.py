from django.shortcuts import render
from django.shortcuts import render,redirect
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .forms import *
# Create your views here.

def home(request):
    if request.user.is_staff:
        context = {

        }
        return render(request, 'index.html',context,)
    if request.user.is_authenticated:
            return render(request, 'director.html')
    else:
        return redirect ("/account/login")



def addmaingas(request):
    if request.user.is_staff:
        if request.method == "POST":
            form = AddMainGasForm(request.POST)
            if form.is_valid():
                f = form.save()
                print(f.mian_gas)
                print(f.buygasprice)
                return redirect('/')
        else:
            form = AddMainGasForm()
            print("NOT " * 5)
        context = {"form":form}
        return render(request, "add_to_gas.html",context)

    else:
        return redirect('/')