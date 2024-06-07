from django import forms
from .models import *
from django.forms.widgets import TextInput,Select

class AddMainGasForm(forms.ModelForm):
    
    class Meta:
        model = Addmaingas
        fields = ("mian_gas","category")
        widgets = {
            "mian_gas":TextInput(attrs={'class':'input',"id":"input_add_gas"}),
            "category":Select(attrs={'class': 'input',"id":"input_add_gas"})
        }
