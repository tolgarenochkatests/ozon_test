""" Задание 3: найти любой товар, вбив название в поисковую строку,
затем положить товар в корзину (не будучи авторизованным, он попросит указать адрес и город).
 Затем надо проверить, что товар в корзине и цена совпадает с итоговой суммой (товар то 1),
 +
 Задача 4: удалить все товары из корзины, перед этим добавив их в Избранное."""
import time

import pytest

from pages.basket_page import BasketPage
from pages.main_page import MainPage


def test_add_to_basket_and_check_price(browser):
    link = "https://www.ozon.ru/"
    page = MainPage(browser, link)
    page.open()
    page.add_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.check_price()


def test_add_to_favorites_and_delete_from_basket(browser):
    link = "https://www.ozon.ru/"
    page = MainPage(browser, link)
    page.open()
    page.add_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.add_to_favorites()
    name = basket_page.take_name()
    basket_page.delete_from_basket()
    basket_page.should_be_empty_basket()
    basket_page.go_to_favorites()
    basket_page.should_be_same_name(name)
