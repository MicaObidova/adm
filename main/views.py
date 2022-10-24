from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
from django.contrib.auth import authenticate, login, logout

def AdsView(request):
    context = {
        'status': Ads.objects.filter(status=1),
        'status2': Ads.objects.filter(status=2),
        'status3': Ads.objects.filter(status=3),
        'status4': Ads.objects.filter(status=4)
    }
    return render(request, "dashboard.html", context)


def AdsStatusDelete(request, pk):
    data = {
        "delete": Ads.status.objects.filter(id=pk).delete()
    }
    return render(request, "dashboard.html", data)


#
# def RecieveAds(request):
#         context = {
#             "active": Ads.status.objects.filter(status=1)
#         }
#         rejected = Ads.status.objects.filter(status=3)
#         rejected.delete()
#         return render(request, "dashboard.html", context)

def InformationView(request):
    return render(request, "information.html")

def add_info(request):
    if request.method == "POST":
        company_name = request.POST.get("company_name")
        logo = request.FILES.get("logo")
        description = request.POST.get("description")
        googleplay = request.POST.get("googleplay")
        appstore = request.POST.get("appstore")
        Information.objects.create(
            company_name=company_name,
            logo=logo,
            description=description,
            googleplay=googleplay,
            appstore=appstore,
        )
    return redirect("information")

def Forlogin(request):
    if request.method == 'POST':
        user = request.user
        username = request.POST.get('username')
        password = request.POST.get('password')
        if user.status == 1 :
            if user.count() > 0:
                usr = authenticate(username=username, password=password)
                if usr is not None:
                    login(request, usr)
                    return redirect('adsview')
                else:
                    return redirect('404')
            else:
                return redirect('404')
        else:
            return redirect('404')
    else:
        return redirect('login-page')


def LogoutView(request):
    logout(request)
    return redirect('login-page')



