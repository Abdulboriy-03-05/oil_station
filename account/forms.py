from django import forms
from .models import User


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(min_length=8, label='Password', widget=forms.PasswordInput(attrs={'placeholder':'parol'}))
    repeat_password = forms.CharField(min_length=8, label='Repeat password', widget=forms.PasswordInput(attrs={'placeholder':'parolni qayta yozing'}))

    class Meta:
        model = User
        fields = ('name','username',"number")
        widgets = {
            "username":forms.widgets.TextInput(attrs={'class':'input', 'placeholder':'Foydalanuvchi nomi', 'autocomplete':"off"}),
            "name":forms.widgets.TextInput(attrs={'class':'input', 'placeholder':'Ismingiz', 'autocomplete':"off"}),
        }



    def clean_repeat_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['repeat_password']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['repeat_password']



