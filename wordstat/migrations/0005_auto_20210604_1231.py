# Generated by Django 3.2.4 on 2021-06-04 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wordstat', '0004_merge_0002_auto_20210602_1406_0003_auto_20210603_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proxy',
            name='datetime_last_used',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Время последнего использования аккаунта'),
        ),
        migrations.AlterField(
            model_name='session',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wordstat.yandexaccount', verbose_name='Яндекс аккаунт'),
        ),
        migrations.AlterField(
            model_name='session',
            name='datetime_last_used',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Время последнего использования аккаунта'),
        ),
        migrations.AlterField(
            model_name='session',
            name='proxy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wordstat.proxy', verbose_name='Прокси'),
        ),
        migrations.AlterField(
            model_name='yandexaccount',
            name='datetime_last_used',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Время последнего использования аккаунта'),
        ),
    ]
