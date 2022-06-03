""" В этом файле хранятся фикстуры, в нашем случае она всего одна -
    - фикстура создания браузера, а потом его закрытия """

import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
