from wordstat.parser_wordstat.proxy import Proxy
import requests
from fake_useragent import UserAgent
from wordstat.parser_wordstat.proxy import proxies
from wordstat.parser_wordstat.cookies import *
from wordstat.models import *
from wordstat.serializers import *
from django.core import serializers
from datetime import datetime
import time
import logging
logging.basicConfig(filename='wordstat/parser_wordstat/log/session.log', level=logging.INFO)
#User-Agent Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36
from wordstat.parser_wordstat.captcha import Captcha
from bs4 import BeautifulSoup


class Parser:
    def __init__(self, session_parser) -> None:
        self.session_parser = session_parser

    def auth_yandex(self):
        logging.info("Аккаунт для запроса: {0} {1}".format(self.session_parser.login_account,
                                                           self.session_parser.password_account))

        logging.info("Прокси для запроса: {0}:{1}".format(self.session_parser.ip, self.session_parser.port))
        print("-----------------------------------------------------------")
        print("Аккаунт для запроса: {0}".format(self.session_parser.login_account))
        print("Прокси для запроса: {0}:{1}".format(self.session_parser.ip, self.session_parser.port))
        print("-----------------------------------------------------------")
        logging.info("-----------------------------------------------------------")
        url = "https://passport.yandex.ru/passport?mode=auth&from=&retpath=https%3A%2F%2Fwordstat.yandex.ru%2F%23!%2Fhistory%3Fwords%3D%25D0%259C%25D0%25B0%25D1%2588%25D0%25B8%25D0%25BD%25D0%25B0&twoweeks=yes"
        self.session_parser.session.get(
            "https://passport.yandex.ru/auth?mode=auth&from=&retpath=https%3A%2F%2Fwordstat.yandex.ru%2F%23!%2Fhistory%3Fwords%3D%25D0%259C%25D0%25B0%25D1%2588%25D0%25B8%25D0%25BD%25D0%25B0&twoweeks=yes")
        time.sleep(1)
        self.session_parser.session.find_elements_by_class_name('Textinput-Control')[0].send_keys(self.session_parser.login_account)
        time.sleep(2)
        self.session_parser.session.find_elements_by_xpath(
            '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[3]/button')[0].click()
        time.sleep(5)
        self.session_parser.session.find_elements_by_class_name('Textinput-Control')[0].send_keys(self.session_parser.password_account)
        time.sleep(5)
        self.session_parser.session.find_elements_by_xpath(
            '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/form/div[3]/button')[0].click()
        time.sleep(3)
        if 'Привяжите номер телефона, чтобы дополнительно защитить свой аккаунт' in self.session_parser.session.page_source:
            self.session_parser.session.find_elements_by_xpath(
                '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/form/div[3]/button')[0].click()
        if 'Доступ к аккаунту ограничен' in self.session_parser.session.page_source:
            return 'Доступ к аккаунту ограничен'
        self.session_parser.session.get('https://wordstat.yandex.ru/')
        # всплывает попап с регионами
        self.session_parser.session.find_element_by_xpath(
            '/html/body/div[1]/table/tbody/tr/td[4]/div/div/form/table/tbody/tr[2]/td[1]/table/tbody/tr/td[2]/div/span').click()
        # переключаемся на него
        self.session_parser.session.switch_to.frame(self.session_parser.session.find_element_by_xpath("//iframe[@class='b-region-select__iframe']"))
        parent_element = self.session_parser.session.find_element_by_xpath('//*[@id="beginRegions"]')
        # перебираем все блоки и подблоки и рааскрывваем списки регионов
        for elem in parent_element.find_elements_by_tag_name('div')[1:]:
            try:
                self.session_parser.session.execute_script("arguments[0].scrollIntoView(true);", elem)
                element = elem.find_element_by_tag_name('a')
                element.click()
            except:
                pass
        return 'Успешно'


    def search(self, data):
        self.session_parser.session_account.is_used = True
        self.session_parser.session_account.save()
        keywords = data['keyrequest']
        regions = data['region']
        # выбрать регионы из списка
        for region in regions:
            region_id = self.session_parser.session.find_element_by_xpath(f"//label[text()='{region}']").get_attribute('for')
            self.session_parser.session.find_element_by_xpath(f"//input[@id='{region_id}']").click()
            print(region_id)

        self.session_parser.session.find_element_by_xpath('/html/body/form/table/tbody/tr[1]/td/div/input[1]').click()
        # переключаемся обратно на родительский фрейм
        self.session_parser.session.switch_to.parent_frame()
        # отправляем в поле ввода ключевые слова
        self.session_parser.session.find_element_by_class_name("b-form-input__input").send_keys(keywords)
        # кликаем по "истории поиска"
        self.session_parser.session.find_element_by_xpath(
            "/html/body/div[1]/table/tbody/tr/td[4]/div/div/form/table/tbody/tr[2]/td[1]/table/tbody/tr/td[1]/ul/li[3]/label/input").click()
        boolean = True
        while boolean:
            try:
                self.session_parser.session.find_element_by_xpath(
                    '/html/body/div[1]/table/tbody/tr/td[4]/div/div/form/table/tbody/tr[1]/td[2]/span/input').click()
            except:
                Captcha(self.session_parser.session).recognize()
            else:
                boolean = False
        soup = BeautifulSoup(self.session_parser.session.page_source)
        data_result = []
        tables = soup.find_all('tbody', class_="b-history__table-body")
        for i in range(2):
            trs = tables[i].find_all('tr')
            for tr in trs:
                res = tr.find_all('td')
                data_result.append([{'totalCount': res[2].text}, {'dates': (res[0].text).replace('\xa0', '')}])
        print(data_result)
        # переключаемся на него
        self.session_parser.session.switch_to.frame(self.session_parser.session.find_element_by_xpath("//iframe[@class='b-region-select__iframe']"))
        # отменить выбор регионы из списка
        for region in regions:
            region_id = self.session_parser.session.find_element_by_xpath(f"//label[text()='{region}']").get_attribute('for')
            self.session_parser.session.find_element_by_xpath(f"//input[@id='{region_id}']").click()
            print(region_id)
        self.session_parser.session.switch_to.parent_frame()
        # очищаем поле ввода
        self.session_parser.session.find_element_by_class_name("b-form-input__input").clear()
        self.session_parser.session_account.datetime_last_used = datetime.now()
        self.session_parser.session_account.is_used = False
        self.session_parser.session_account.save()
        return data_result