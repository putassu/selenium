from anticaptchaofficial.imagecaptcha import *
from Parser import settings
import os


class Captcha:
    def __init__(self, driver):
        self.driver = driver

    def recognize(self):
        img_src = self.driver.find_elements_by_class_name('b-popupa__image')[0].get_attribute('src')
                # запрашиваем по ссылке капчу
        r = requests.get(img_src)

                # открываем и записываем капчу в файл jpg кусочками по 1000 байт
        with open("file.jpg", 'wb') as fd:
            for chunk in r.iter_content(1000):
                fd.write(chunk)
                # распознаем капчу и записываем в переменную answer
        path_image = (f"{img_src[-20:-1]}.jpg")
        solver = imagecaptcha.imagecaptcha()
        solver.set_verbose(1)
        solver.set_key(settings.TOKEN)
        captcha_text = solver.solve_and_return_solution(path_image)
        if captcha_text != 0:
            return captcha_text
        else:
            return solver.error_code
                    # удаляем картинку с капчой
        os.path("file.jpg").remove()
                    # вводим ответ в поле
        self.driver.find_element_by_css_selector("#uniq162391574795292").send_keys(answer)
                    # отправляем
        self.driver.find_element_by_xpath('/html/body/div[7]/div/div/table/tbody/tr/td/div/form/table/tbody/tr[2]/td[2]/span/input').click()
        time.sleep(3)



"""
ymex=1936684063.yrts.1621324063#1936684063.yrtsi.1621324063; fuid01=60a3711f64c4b9fb.slS_nVHjPnTsCk6Uw2HzZhGW_SwXfj6lpVXyN3pyjrrhGWF1hW1eR-0cl7uM-6zVOqT0jtn-m6wMokmOuiczpi28SNMaLPziEVqT0GUeVonxPfU-d2_S0_MdUy3ukiyc; gdpr=0; _ym_uid=161858020691311743; is_gdpr=0; mda=0; yandex_gid=39; is_gdpr_b=CO2OPxCXLygC; yandexuid=6033038781618580204; yuidss=6033038781618580204; my=YwA=; stngs=stngs.1:colorful::true:true; ymai_iale=0; amcuid=8832764341621404902; Session_id=3:1622631616.5.1.1621324073468:BBPhQA:19.1|1130000052004767.0.2|1427714847.1307543.2.2:1307543|235445.828276.u7bn6e3QHkUNF5fDqD0WZR6tEIo; sessionid2=3:1622631616.5.1.1621324073468:BBPhQA:19.1|1130000052004767.0.2|1427714847.1307543.2.2:1307543|235445.828276.u7bn6e3QHkUNF5fDqD0WZR6tEIo; yp=1937991616.udn.cDpzdXBlcmlvcml0eTEwMQ==#1623934095.ygu.1#1637110098.szm.1:1920x1080:1853x981#1624021186.csc.1#1621947591.mcv.0#1621947591.mct.null#1621947591.mcl.1t171ej#1622023575.nwcst.1621943400_39_1#1937991616.multib.1; L=WDV7YmBgCnV0R0ZcRlVLdlELVktnA0ABHw0WFisaA0AYFjIEWmQ=.1622631616.14620.366336.218a262a317d3c7d9a4b83b4215e7207; yandex_login=superiority101; _ym_d=1622631753; zm=m-white_bender-redesign.webp.css-https:s3home-static_3FmHACE5EQmZuVGBYjwPeTB5Jdk:l; yabs-frequency=/5/0G0004Mwes000000/5r91ROO0000eGISa841jXW0002X18O9XGMs60000A44Z/; i=KHi1lTGfCpyc8rR4XHfcsc/EGeZ1LRW3gFb9O/WEm5LawXzI4RbkvnOwWfHtxcVrC+Qzm8ONTpmPjLgNQ5OgxQP7BoA=; _gcl_au=1.1.1548255130.1622640556; _ym_isad=2; app_badge_up_to_date_1130000052004767=1; cycada=+JPQIZNI46dOp7LLxZ2NHOQnSjOrbLKrZ8C6+ZYaWTg=
ymex=1936684063.yrts.1621324063#1936684063.yrtsi.1621324063; fuid01=60a3711f64c4b9fb.slS_nVHjPnTsCk6Uw2HzZhGW_SwXfj6lpVXyN3pyjrrhGWF1hW1eR-0cl7uM-6zVOqT0jtn-m6wMokmOuiczpi28SNMaLPziEVqT0GUeVonxPfU-d2_S0_MdUy3ukiyc; gdpr=0; _ym_uid=161858020691311743; is_gdpr=0; mda=0; yandex_gid=39; is_gdpr_b=CO2OPxCXLygC; yandexuid=6033038781618580204; yuidss=6033038781618580204; my=YwA=; amcuid=8832764341621404902; Session_id=3:1622631616.5.1.1621324073468:BBPhQA:19.1|1130000052004767.0.2|1427714847.1307543.2.2:1307543|235445.828276.u7bn6e3QHkUNF5fDqD0WZR6tEIo; sessionid2=3:1622631616.5.1.1621324073468:BBPhQA:19.1|1130000052004767.0.2|1427714847.1307543.2.2:1307543|235445.828276.u7bn6e3QHkUNF5fDqD0WZR6tEIo; yp=1937991616.udn.cDpzdXBlcmlvcml0eTEwMQ==#1623934095.ygu.1#1637110098.szm.1:1920x1080:1853x981#1624021186.csc.1#1621947591.mcv.0#1621947591.mct.null#1621947591.mcl.1t171ej#1622023575.nwcst.1621943400_39_1#1937991616.multib.1; L=WDV7YmBgCnV0R0ZcRlVLdlELVktnA0ABHw0WFisaA0AYFjIEWmQ=.1622631616.14620.366336.218a262a317d3c7d9a4b83b4215e7207; yandex_login=superiority101; _ym_d=1622631753; zm=m-white_bender-redesign.webp.css-https:s3home-static_3FmHACE5EQmZuVGBYjwPeTB5Jdk:l; yabs-frequency=/5/0G0004Mwes000000/5r91ROO0000eGISa841jXW0002X18O9XGMs60000A44Z/; i=KHi1lTGfCpyc8rR4XHfcsc/EGeZ1LRW3gFb9O/WEm5LawXzI4RbkvnOwWfHtxcVrC+Qzm8ONTpmPjLgNQ5OgxQP7BoA=; _gcl_au=1.1.1548255130.1622640556; cycada=dqM4FVLsQ85Rx57TolPR0eQnSjOrbLKrZ8C6+ZYaWTg=; _ym_isad=2; wsst=701d3a12d5f2b2688f78535c1e23d1392|60b8b640
"""