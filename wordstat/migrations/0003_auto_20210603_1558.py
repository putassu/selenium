# Generated by Django 3.2.3 on 2021-06-02 10:27

from django.db import migrations, models


def proxy(apps, schema_editor):
    # Типы - наш перечень, который будет вставлен в БД
    proxies = [
        {"ip": "91.107.119.18", "port": "34512", "login": "achuhrajI3", "password": "F2f0LeZ"},
        {"ip": "89.191.227.143", "port": "34512", "login": "achuhrajI3", "password": "F2f0LeZ"},
        {"ip": "193.233.80.125", "port": "34512", "login": "achuhrajI3", "password": "F2f0LeZ"},
        {"ip": "185.30.99.106", "port": "34512", "login": "achuhrajI3", "password": "F2f0LeZ"},
        {"ip": "5.180.103.105", "port": "34512", "login": "achuhrajI3", "password": "F2f0LeZ"},
        {"ip": "176.53.132.68", "port": "34512", "login": "achuhrajI3", "password": "F2f0LeZ"},
        {"ip": "77.220.205.48", "port": "34512", "login": "achuhrajI3", "password": "F2f0LeZ"},
        {"ip": "85.117.233.45", "port": "34512", "login": "achuhrajI3", "password": "F2f0LeZ"},
        {"ip": "31.148.99.157", "port": "34512", "login": "achuhrajI3", "password": "F2f0LeZ"},
        {"ip": "46.16.13.93", "port": "34512", "login": "achuhrajI3", "password": "F2f0LeZ"},
    ]
    # Попросим Django вытащить модель - класс ClientTypes из аппликейшена user_profile
    Proxy = apps.get_model("wordstat", "Proxy")

    # Теперь в цикле создаём экземпляры класса с указанными параметрами и сохраняем их
    for proxy in proxies:
        cl_type = Proxy(ip=proxy["ip"], port=proxy["port"], login=proxy["login"], password=proxy["password"])
        cl_type.save()


class Migration(migrations.Migration):
    dependencies = [
        ('wordstat', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(proxy)
    ]
