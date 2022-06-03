""" Это прародитель всех классов страниц. Отсюда наследуется основной функционал:
        открытие страницы, проверка на поиск элемента на ней"""

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, browser, url, timeout=4):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def go_to_page(self, locator):
        link = self.browser.find_element(By.LINK_TEXT, locator)
        link.click()