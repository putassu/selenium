import requests
from datetime import datetime
from fake_useragent import UserAgent
import logging
from wordstat.models import *
from wordstat.serializers import *
from selenium import webdriver


class SessionObject:
    def __init__(self):
        if len(Session.objects.filter(is_used=False).order_by("datetime_last_used")) == 0:
            account = YandexAccount.objects.filter(active=True).order_by("datetime_last_used")[0]
            account.datetime_last_used = datetime.now()
            account.save()
            proxy = Proxy.objects.filter(active=True).order_by("datetime_last_used")[0]
            proxy.datetime_last_used = datetime.now()
            proxy.save()
            self.session_account = Session(account=account, proxy=proxy, is_used=True)
            self.session_account.save()
            self.login_account = account.login
            self.password_account = account.password
            "http://user:pw@proxy:8080"
            self.method_proxy = "https://"
            self.login_proxy = proxy.login
            self.password_proxy = proxy.password
            self.ip = proxy.ip
            self.port = proxy.port
        else:
            self.session_account = Session.objects.filter(is_used=False).order_by("datetime_last_used")[0]
            self.login_account = self.session_account.account.login
            self.password_account = self.session_account.account.password
            self.method_proxy = "https"
            self.login_proxy = self.session_account.proxy.login
            self.password_proxy = self.session_account.proxy.password
            self.ip = self.session_account.proxy.ip
            self.port = self.session_account.proxy.port

            self.session_account.is_used = True
            self.session_account.save()

        self._proxy = self.method_proxy + self.login_account + ":" + self.password_proxy + "@" + self.ip + ":" + \
                      str(self.port)
        self.session = webdriver.Firefox()

