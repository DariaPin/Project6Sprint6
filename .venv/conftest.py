import pytest
from selenium import webdriver
from data import Urls


@pytest.fixture(scope='function')
def driver():


    browser = webdriver.Firefox()

    browser.get(Urls.SAMOKAT_URL)

    yield browser

    browser.quit()