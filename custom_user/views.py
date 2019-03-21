# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from .forms import RegisterForm, LoginForm
from .models import UserProfile
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
class RegisterView(View):

    def get(self, request):
        return render(request, "register.html", {"request": request})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("uname")
            if UserProfile.objects.filter(username=user_name):
                return render(request, "register.html", {"register_form": register_form, "msg": "Username already exists!"})
            email = request.POST.get("email")
            mobile = request.POST.get("mobile")
            pwd = request.POST.get("pwd")
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = email
            user_profile.mobile = mobile
            user_profile.is_active = True
            user_profile.set_password(pwd)
            
           
            # user_profile.password = make_password(pwd)
            user_profile.save()
            return render(request, "login.html")
        else:
            return render(request, "register.html", {"register_form": register_form,"request": request})


class LogoutView(View):
    
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("home"))


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

def facebook(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        login(request, user)
    else:
        user = User.objects.create_user(username=username, password='facebook')
        user.save()
        user = authenticate(username=username, password='facebook')
        login(request, user)
    return HttpResponseRedirect(reverse("home"))

class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {"request": request})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("uname", "")
            pass_word = request.POST.get("pwd", "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse("home"))
                else:
                    return render(request, "login.html", {"msg": "User is not activated！"})
            else:
                return render(request, "login.html", {"msg": "Username or password is wrong！"})
        else:
            return render(request, "login.html", {"login_form": login_form, "request": request})


class DetailView(View):
    def get(self, request):
        return render(request, "detail.html", {"request": request})

    def post(self, request):
        user = UserProfile.objects.get(username=request.user.username)
        mobile = request.POST.get("mobile", "")
        wechat = request.POST.get("wechat", "")
        location = request.POST.get("location", "")
        user.mobile = mobile
        user.wechat = wechat
        user.location = location
        user.save()
        return render(request, "detail.html", {"request": request})




