from django.db import models


class YandexAccount(models.Model):
    login = models.CharField(max_length=100, verbose_name="Логин")
    password = models.CharField(max_length=100, verbose_name="Пароль")
    count_captcha = models.IntegerField(blank=True, null=True, verbose_name="Количество появлений каптч", default=0)
    active = models.BooleanField(default=True, verbose_name="Статус не заблокирован ли аккаунт")
    datetime_last_used = models.DateTimeField(blank=True, null=True, auto_now_add=True,
                                              verbose_name="Время последнего использования аккаунта")

    class Meta:
        verbose_name = "Яндекс аккаунт"
        verbose_name_plural = "Яндекс аккаунты"
        ordering = ("datetime_last_used",)

        def __str__(self) -> str:
            return self.login


class Proxy(models.Model):
    ip = models.CharField(max_length=15, blank=False, null=False, verbose_name="IP прокси")
    port = models.IntegerField(blank=False, null=False, verbose_name="Порт прокси")
    login = models.TextField(blank=False, null=False, verbose_name="Логин от прокси сервера")
    password = models.TextField(blank=False, null=False, verbose_name="Пароль от прокси сервера")
    datetime_last_used = models.DateTimeField(blank=True, null=True, auto_now_add=True,
                                              verbose_name="Время последнего использования аккаунта")
    active = models.BooleanField(default=True, verbose_name="Статус не заблокирован ли прокси")

    class Meta:
        verbose_name = "Прокси"
        verbose_name_plural = "Прокси"
        ordering = ("datetime_last_used",)

        def __str__(self) -> str:
            return self.ip


class Session(models.Model):
    account = models.ForeignKey("YandexAccount", on_delete=models.PROTECT, verbose_name="Яндекс аккаунт")
    proxy = models.ForeignKey("Proxy", on_delete=models.PROTECT, verbose_name="Прокси")
    datetime_last_used = models.DateTimeField(blank=True, null=True, auto_now_add=True,
                                              verbose_name="Время последнего использования аккаунта")
    is_used = models.BooleanField(default=False, verbose_name="Статус используется ли сессия")

    class Meta:
        verbose_name = "Сессия"
        verbose_name_plural = "Сессии"

        def __str__(self) -> str:
            return self.account
