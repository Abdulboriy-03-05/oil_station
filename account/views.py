from django.shortcuts import render
from django.shortcuts import redirect, render
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import *
from .models import User
# Create your views here.
# class ProfileView(LoginRequiredMixin, DetailView):
#     model = User
#     template_name = 'main/profile.html'

#     def get_object(self):
#         user = User.objects.get(id=self.request.user.id)
#         return user


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            auth.login(request,user)
            return redirect('/')
    else:
        form = UserRegisterForm()
    return render(request, "main/register.html", {"form":form})