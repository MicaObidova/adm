from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
         model = User
         fields = "__all__"


class AdsSerializer(serializers.ModelSerializer):
    class Meta:
         model = Ads
         fields = "__all__"


class AdsStatusDeleteSerializer(serializers.ModelSerializer):
    class Meta:
         model = Ads
         fields = "__all__"


class RecieveAdsSerializer(serializers.ModelSerializer):
    class Meta:
         model = Ads
         fields = "__all__"


class InformationSerializer(serializers.ModelSerializer):
    class Meta:
         model = Information
         fields = "__all__"

