from rest_framework import serializers
from wordstat.models import *
from django.contrib.auth.hashers import make_password


class QuerySerialize(serializers.Serializer):
    keyrequest = serializers.CharField(required=True, help_text="Words to request")
    region = serializers.CharField(default=225, help_text="ID of the region, by default Russia")  # Default Russia


class YandexAccountSerialize(serializers.ModelSerializer):
    class Meta:
        model = YandexAccount
        fields = ("id", "login", "password", "count_captcha", "active")


class ProxySerialize(serializers.ModelSerializer):
    class Meta:
        model = Proxy
        fields = ("id", "ip", "port", "login", "password", "datetime_last_used", "active")


class SessionSerialize(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ("id", "account", "proxy", "datetime_last_used", "is_used")

