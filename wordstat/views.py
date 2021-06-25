from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.serializers import ValidationError
from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework.permissions import *
from rest_framework import generics

from drf_yasg.utils import swagger_auto_schema
from wordstat.serializers import *
from Parser.settings import *
from wordstat.parser_wordstat.getdata import get_history_data
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from wordstat.parser_wordstat.parse import Parser

from wordstat.models import *
import time


#if not auth:
#    return AUTH_ERROR

#@method_decorator(csrf_exempt, name='dispatch')
@swagger_auto_schema(method="post", request_body=QuerySerialize)
@api_view(["POST"])
def get_history(request):


    if request.method == "POST":
        validate(request.data)
        serializer = QuerySerialize(request.data)
        data = get_history_data(serializer.data)
        print(data)
        print("========================================================================================================")
        #time.sleep(5)
        #data1 = get_history_data(serializer.data)
        #print(data1)
        #print("========================================================================================================")
        #time.sleep(5)
        #data2 = get_history_data(serializer.data)
        #print(data2)
        #time.sleep(8)
        #data = get_history_data(serializer.data

        #if data == AUTH_ERROR:
        #    content = {"Error yandex auth": "Incorrect login or password"}
        #   return Response(content, status.HTTP_400_BAD_REQUEST)
        if data == FIND_ERROR:
            content = {"Nothing found": "No results were found for your search"}
            return Response(content, status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data)


class YandexAccountList(generics.ListCreateAPIView):
    queryset = YandexAccount.objects.all()
    serializer_class = YandexAccountSerialize


class YandexAccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = YandexAccount.objects.all()
    serializer_class = YandexAccountSerialize


class ProxyList(generics.ListCreateAPIView):
    queryset = Proxy.objects.all()
    serializer_class = ProxySerialize


class ProxyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proxy.objects.all()
    serializer_class = ProxySerialize


class SessionList(generics.ListCreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerialize


class SessionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerialize


def validate(data):
    if 'keyrequest' not in data:
        raise ValidationError(['keyrequest field is required.'])


