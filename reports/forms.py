from django import forms
from .models import *
from django.forms.widgets import TextInput

class AddMainGasForm(forms.ModelForm):
    
    class Meta:
        model = Addmaingas
        fields = ("mian_gas","buygasprice",)
        exclude = ['gas',"salegasprice","cardprofid"]
        widgets = {
            "mian_gas":TextInput(attrs={'class':'input',"id":"input_add_gas"}),
            "buygasprice":TextInput(attrs={'class':'input',"id":"input_add_gas"}),
        }