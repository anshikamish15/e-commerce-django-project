from django.shortcuts import render, redirect
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail

import random

def home(request):
    return render(request, "index.html")

def signup(request):
    if request.method == "POST":
        a = request.POST['first']
        b = request.POST['last']
        c = request.POST['role']
        d = request.POST['email']
        e = request.POST['mobile']
        f = request.POST['password']
        g = request.POST['username']

        u = User(username=g, password=make_password(f), first_name=a, last_name=b, email=d)
        u.save()

        up = UserProfile(user=u, mobile=e, role=c)
        up.save()

    return render(request, "signup.html")

def login_call(request):
    if request.method == "POST":
        h = request.POST['username']
        i = request.POST['pwd']

        user = authenticate(username=h, password=i)

        if user:
            login(request, user)
            uObj = UserProfile.objects.get(user__username=request.user)

            if uObj.role == "Seller":
                return redirect('/seller/home')
            elif uObj.role == "Buyer":
                return redirect('/buyer/home')
            else:
                return redirect('/login/')
        else:
            return redirect('/login/')


    return render(request, "login.html")

def forgot(request):

    code = random.randint(1000, 9999)
    send_mail("Reset Link", str(code), "gpmishra9@gmail.com",["anshika97mishra@gmail.com",])

    if request.method == "POST":
        v = request.POST['code']

        if code == v:
            paswd = request.POST['password']
            uObj = UserProfile.objects.get(user__username=request.user)
            u = User.objects.get(id = uObj.user_id)
            u.update(password = paswd)
            u.save()
        else:
            return redirect('/forgotpassword/')


    return render(request, "reset_password.html")

def reset_password(request):
    if request.method == "POST":
        j = request.POST['password']

        u = User(password=make_password(j))
        u.save()
        return redirect('/login/')
    return render(request, "reset_password.html")


def logout_call(request):
    logout(request)
    return redirect('/login/')