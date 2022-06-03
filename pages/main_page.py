""" Это класс главной страницы (на которую кидает при переходе на https://www.ozon.ru/)"""

import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from .base_page import BasePage
import requests
from .locators import MainLocators, BasketLocators


class MainPage(BasePage):
    def should_status_be_ok(self):
        link = self.browser.current_url
        assert requests.get(link).status_code == 200, "Status is not 200"

    def should_be_element_on_page(self, how, what):
        assert self.is_element_present(how, what), "No content"

    def scroll_to_elem(self, how, what):
        self.browser.execute_script("arguments[0].scrollIntoView();", self.browser.find_element(how, what))

    def find_img_link_and_check(self, how, what):
        img = self.browser.find_element(how, what)
        src = img.get_attribute("src")
        assert requests.get(src).status_code == 200, "No img"

    def add_to_basket(self):
        self.browser.find_element(*MainLocators.FIND_INPUT).send_keys("часы" + Keys.ENTER)
        self.browser.find_element(*MainLocators.ADD_BASKET_BUT).click()
        time.sleep(2)
        try:
            self.browser.find_element(*MainLocators.ALERT_ADRES).send_keys("шоссе Фрезер, 7/2, Москва, Россия")
            time.sleep(1)
            self.browser.find_element(*MainLocators.ALERT_ADRES_LI).click()
            time.sleep(2)
            self.browser.find_element(*MainLocators.ALERT_ADRES_BUT).click()
            time.sleep(2)
        except:
            pass
        finally:
            self.browser.find_element(*MainLocators.BASKET_BUT).click()
            self.browser.find_element(*BasketLocators.ALERT_CLOSE_BUT).click()
            time.sleep(2)
