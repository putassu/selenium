from django.contrib import admin
from wordstat.models import *


class YandexAccountAdmin(admin.ModelAdmin):
    fields = ['login', 'password', 'count_captcha', 'active']
    list_display = ('login', 'password', 'count_captcha', 'active', 'datetime_last_used')
    search_fields = ['login']
    list_filter = ['active']


class ProxyAdmin(admin.ModelAdmin):
    fields = ['ip', 'port', 'login', 'password', 'active']
    list_display = ('ip', 'port', 'login', 'password', 'datetime_last_used', 'active')
    search_fields = ['ip']
    list_filter = ['active']


class SessionAdmin(admin.ModelAdmin):
    fields = ['account', 'proxy', 'is_used']
    list_display = ('account', 'proxy', 'datetime_last_used', 'is_used')
    search_fields = ['account']
    list_filter = ['is_used']


admin.site.register(YandexAccount, YandexAccountAdmin)
admin.site.register(Proxy, ProxyAdmin)
admin.site.register(Session, SessionAdmin)
