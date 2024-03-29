# Generated by Django 3.2.3 on 2021-06-02 10:27

from django.db import migrations, models

def yandex_accounts(apps, schema_editor):
    # Типы - наш перечень, который будет вставлен в БД
    accounts = [
        {"login": "superiority101@yandex.ru", "password": "321-Vcxz1"},
        {"login": "superiority102@yandex.ru", "password": "321-Vcxz1"},
    ]
    # Попросим Django вытащить модель - класс ClientTypes из аппликейшена user_profile
    YandexAccount = apps.get_model("wordstat", "YandexAccount")
    
    #Теперь в цикле создаём экземпляры класса с указанными параметрами и сохраняем их 
    for account in accounts:
        cl_type = YandexAccount(login=account["login"], password=account["password"])
        cl_type.save()


class Migration(migrations.Migration):

    dependencies = [
        ('wordstat', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(yandex_accounts)
    ]
