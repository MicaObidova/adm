from django.urls import path
from .views import *



urlpatterns = [
    path("", AdsView, name="adsview"),
    path("adsstatusdelete/", AdsStatusDelete, name="adsstatusdelete"),
    path("recieveads", RecieveAds, name="receiveads"),
    path("information", InformationView, name="information"),
    path("add-info", add_info, name="add-info"),
    # path('delete-region/<int:pk>/', de)
    # path("register/", register, name="register")
]