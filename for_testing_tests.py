""" Этот файл сугубо для проверки каких-то отдельных компонентов, тут нет ничего интересного"""

import time
import requests
import selenium
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.locators import MainLocators, BasketLocators

link = "https://www.ozon.ru/"
# # print(requests.get(link).content)
driver = webdriver.Chrome()
driver.get(link)
time.sleep(5)
# driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.XPATH, "//*[contains(text(), 'Успей купить!')]"))
#
# img = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[4]/div[1]/div[1]/div[7]/div[2]/a[1]/img")
# src = img.get_attribute("src")
# print(src)
#
# res = requests.get(src)
# print(res.status_code)

driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(*MainLocators.USPEI_KUPIT_LINK))
driver.find_element(By.XPATH, "")
time.sleep(4)

