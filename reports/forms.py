from django import forms
from .models import *
from django.forms.widgets import TextInput,Select

class AddMainGasForm(forms.ModelForm):
    
    class Meta:
        model = Addmaingas
        fields = ("last_gas","category")
        widgets = {
            "last_gas":TextInput(attrs={'class':'number',"type":"number","id":"input_add_gas"}),
            "category":Select(attrs={'class': 'input',"id":"input_add_gas"})
        }

class AddExtraGasForm(forms.ModelForm):
    
    class Meta:
        model = Addmaingas
        fields = ("last_gas","category","date")
        widgets = {
            "category":Select(attrs={'class': 'input',"id":"input_add_gas"}),
            "last_gas":TextInput(attrs={'class':'input',"type":"number","id":"input_add_gas"}),
            "date":TextInput(attrs={'class':'input',"type":"date","id":"input_add_gas"}),
        }

class Addbank(forms.ModelForm):
    
    class Meta:
        model = Addmaingas
        fields = ("naqt","uzcard","humo")
        widgets = {
            "naqt":forms.CheckboxInput(attrs={'class':'checkbox',}),
            "uzcard":forms.CheckboxInput(attrs={'class':'checkbox',}),
            "humo":forms.CheckboxInput(attrs={'class':'checkbox',}),
        }



class AddIncomeForm(forms.ModelForm):
    
    class Meta:
        model = Income_XRS
        fields = "__all__"
        widgets = {
            "sum":TextInput(attrs={'class':'input',"type":"number","id":"input_add_gas"}),
            "category":Select(attrs={'class': 'input',"id":"input_add_gas"}),
            "income":Select(attrs={'class': 'input',"id":"input_add_gas"}),
            "description":forms.Textarea(attrs={'class':'input',"id":"input_add_gas"}),

            
        }



class AdditionalmoneyForm(forms.ModelForm):
    
    class Meta:
        model = Main_XR_income
        fields = "__all__"
        exclude = ["date"]
        widgets = {
            "category":Select(attrs={'class': 'input',"id":"input_add_gas"}),
            "income":TextInput(attrs={'class':'input',"type":"number","id":"input_add_gas"}),
            "description":TextInput(attrs={'class':'input',"id":"input_add_gas"}),
            
        }

class CareditPayForm(forms.ModelForm):
    
    class Meta:
        model = Credit_income
        fields = "__all__"
        exclude = ["date"]
        widgets = {
            "category":Select(attrs={'class': 'input',"id":"input_add_gas"}),
            "dollar":TextInput(attrs={'class':'input',"type":"number","id":"input_add_gas"}),
            "income":TextInput(attrs={'class':'input',"type":"number","id":"input_add_gas"}),
        }



class Stationsalegas_6(forms.ModelForm):
    
    class Meta:
        model = Manag_add_gas
        fields = "__all__"
        exclude = ['user','category','total_gas','kalonka_8','kalonka_7','remain_gas', "lose_gas","gas" ,"date","total_sum"]
        widgets = {
            "kalonka_1":TextInput(attrs={'class':'input',"type":"number","id":"input_add_gas"}),
            "kalonka_2":TextInput(attrs={'class':'input',"type":"number","id":"input_add_gas"}),
            "kalonka_3":TextInput(attrs={'class':'input',"type":"number","id":"input_add_gas"}),
            "kalonka_4":TextInput(attrs={'class':'input',"type":"number","id":"input_add_gas"}),
            "kalonka_5":TextInput(attrs={'class':'input',"type":"number","id":"input_add_gas"}),
            "kalonka_6":TextInput(attrs={'class':'input',"type":"number","id":"input_add_gas"}),

            
        }



class Stationsalegas_8(forms.ModelForm):
    
    class Meta:
        model = Manag_add_gas
        fields = "__all__"
        exclude = ['user','category','total_gas','remain_gas',"lose_gas","gas","date","total_sum"]
        widgets = {
            "kalonka_1":TextInput(attrs={'class':'input',"type":"number","id":"input_add_gas"}),
            "kalonka_2":TextInput(attrs={'class':'input',"type":"number","id":"input_add_gas"}),
            "kalonka_3":TextInput(attrs={'class':'input',"type":"number","id":"input_add_gas"}),
            "kalonka_4":TextInput(attrs={'class':'input',"type":"number","id":"input_add_gas"}),
            "kalonka_5":TextInput(attrs={'class':'input',"type":"number","id":"input_add_gas"}),
            "kalonka_6":TextInput(attrs={'class':'input',"type":"number","id":"input_add_gas"}),
            "kalonka_7":TextInput(attrs={'class':'input',"type":"number","id":"input_add_gas"}),
            "kalonka_8":TextInput(attrs={'class':'input',"type":"number","id":"input_add_gas"}),

            
        }


class Stationaddgas(forms.ModelForm):
    
    class Meta:
        model = Manag_totals
        fields = ("card_uz","card_humo","company")
        widgets = {
            "card_uz":TextInput(attrs={'class':'input',"type":"number","id":"input_add_gas"}),
            "card_humo":TextInput(attrs={'class':'input',"type":"number","id":"input_add_gas"}),
            "company":TextInput(attrs={'class':'input',"type":"number","id":"input_add_gas"}),
        }



class GetMoneyeachForm(forms.ModelForm):
    
    class Meta:
        model = Borrow_money
        fields = "__all__"
        exclude = ["date"]
        widgets = {
            "bring_money":Select(attrs={'class': 'input',"id":"input_add_gas"}),
            "get_money":Select(attrs={'class': 'input',"id":"input_add_gas"}),
            "bill":TextInput(attrs={'class':'input',"type":"number","id":"input_add_gas"}),

            
        }

