""" Класс страницы корзины"""
import time

from pages.base_page import BasePage
from pages.locators import BasketLocators


class BasketPage(BasePage):
    def check_price(self):
        exp = self.browser.find_element(*BasketLocators.PRICE_LOCATOR).text
        real = self.browser.find_element(*BasketLocators.TOTAL_PRICE_LOCATOR).text
        assert exp == real, "Bad price"

    def add_to_favorites(self):
        self.browser.find_element(*BasketLocators.ADD_TO_FAVORITES_BUT).click()

    def delete_from_basket(self):
        self.browser.find_element(*BasketLocators.DELETE_FROM_BASKET_BUT).click()
        time.sleep(1)
        self.browser.find_element(*BasketLocators.DELETE_CONFIRM_BUT).click()
        time.sleep(1)

    def should_be_empty_basket(self):
        assert self.is_element_present(*BasketLocators.EMPTY_TEXT), "No message about empty basket"

    def take_name(self):
        return self.browser.find_element(*BasketLocators.NAME).text

    def go_to_favorites(self):
        self.browser.find_element(*BasketLocators.FAVORITES_BUT).click()

    def should_be_same_name(self, text):
        name = self.browser.find_element(*BasketLocators.FAVORITES_NAME).text
        assert name == text


