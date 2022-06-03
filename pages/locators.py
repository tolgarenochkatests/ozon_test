""" Здесь хранятся локаторы различных элементов, чтобы в случае изменения объекта
        можно было вносить изменения только в этот файл"""

from selenium.webdriver.common.by import By


class HeaderLocators:
    TOP_FASHION_LINK = By.CLASS_NAME, "a8nb"
    PREMIUM_LINK = By.CLASS_NAME, "n6z"
    TICKETS_LINK = By.CLASS_NAME, "zc"
    OZON_FRESH_LINK = By.CLASS_NAME, "a8nb"
    LIVE_LINK = By.CLASS_NAME, "h0s"
    SALE_LINK = By.CLASS_NAME, "a8nb"
    BRAND_LINK = By.CLASS_NAME, "bqa1"
    STORES_LINK = By.CLASS_NAME, "p2i"
    ELECTRONICS_LINK = By.CLASS_NAME, "pba0"
    CLOTHES_AND_SHOES_LINK = By.CLASS_NAME, "a8nb"
    KIDS_LINK = By.CLASS_NAME, "pba0"


class ImgLocators:
    IMG1 = By.XPATH, "//div[7]/div[2]/div/div/a/img"
    IMG2 = By.XPATH, "//div[7]/div[2]/div/div/a[1]/img"
    IMG3 = By.XPATH, "//div[7]/div[2]/div/div/a[2]/img"
    IMG4 = By.XPATH, "//div[7]/div[2]/div/div/a[3]/img"


# Да простят меня все за хpathы, тут по-другому никак(((

class MainLocators:
    USPEI_KUPIT_LINK = By.XPATH, "//*[contains(text(),'Успей купить!')]"
    FIND_INPUT = By.XPATH, "//*[@id='stickyHeader']/div[3]/div/form/div[2]/input[1]"
    ADD_BASKET_BUT = By.XPATH, "//*[.='В корзину']"
    BASKET_BUT = By.CLASS_NAME, "pa"
    ALERT_CLOSE_BUT = By.XPATH, "//div[3]/div/button"
    ALERT_ADRES_BUT = By.XPATH, "//div[2]/div/div/div/div[2]/div/div/button"
    ALERT_ADRES = By.XPATH, "//label/div[1]/div/input"
    ALERT_ADRES_LI = By.XPATH, "//label/ul/li[1]"


class BasketLocators:
    ALERT_CLOSE_BUT = By.XPATH, "//div[3]/div/button"
    PRICE_LOCATOR = By.XPATH, "//div[3]/span[1]/span"
    TOTAL_PRICE_LOCATOR = By.XPATH, "//div[4]/span[2]"
    ADD_TO_FAVORITES_BUT = By.XPATH, "//*[.='B избранное']"
    DELETE_FROM_BASKET_BUT = By.XPATH, "//*[contains(text(),'Удалить выбранные')]"
    DELETE_CONFIRM_BUT = By.XPATH, "//section/div[3]/div/button"
    EMPTY_TEXT = By.XPATH, "//*[.='Корзина пуста']"
    NAME = By.XPATH, "//div[2]/a/span[1]/span"
    FAVORITES_BUT = By.XPATH, "//*[@id='stickyHeader']/div[4]/a[1]"
    FAVORITES_NAME = By.XPATH, "//div[1]/div[1]/a/span/span"