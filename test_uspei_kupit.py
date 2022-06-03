""" Задание 2: на главной странице есть категория "Успей купить" (ниже листать надо).
Контент подгружается при прокрутке страницы, а не сразу. Нужно проверить,
что все картинки категорий "Успей купить" отображаются (а не белый квадрат). """

import pytest
from pages.locators import ImgLocators
from pages.locators import MainLocators
from pages.main_page import MainPage


@pytest.mark.parametrize("elem", [ImgLocators.IMG1, ImgLocators.IMG2, ImgLocators.IMG3, ImgLocators.IMG4])
def test_is_img_display(browser, elem):
    link = "https://www.ozon.ru/"
    page = MainPage(browser, link)
    page.open()
    page.scroll_to_elem(*MainLocators.USPEI_KUPIT_LINK)
    page.find_img_link_and_check(*elem)
