""" Задание 1: нужно пробежаться по ссылкам в шапке (Билеты и отели, Premium, Акции и тд)
и проверить, что все ссылки отдают 200, кликабельны и страницы загружаются после перехода
 (что контент реально отображается)"""

import pytest
from pages.main_page import MainPage
from pages.locators import HeaderLocators


@pytest.mark.parametrize("locator, elem", [("TOP Fashion", HeaderLocators.TOP_FASHION_LINK),
                                           ("Premium", HeaderLocators.PREMIUM_LINK),
                                           ("Билеты и Отели", HeaderLocators.TICKETS_LINK),
                                           ("Ozon fresh", HeaderLocators.OZON_FRESH_LINK),
                                           ("LIVE", HeaderLocators.LIVE_LINK),
                                           ("Акции", HeaderLocators.SALE_LINK),
                                           ("Бренды", HeaderLocators.BRAND_LINK),
                                           ("Магазины", HeaderLocators.STORES_LINK),
                                           ("Электроника", HeaderLocators.ELECTRONICS_LINK),
                                           ("Одежда и обувь", HeaderLocators.CLOTHES_AND_SHOES_LINK),
                                           ("Детские товары", HeaderLocators.KIDS_LINK)])
def test_headers_status_and_content(browser, locator, elem):
    link = "https://www.ozon.ru/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_page(locator)
    # page.should_status_be_ok()
    page.should_be_element_on_page(*elem)
