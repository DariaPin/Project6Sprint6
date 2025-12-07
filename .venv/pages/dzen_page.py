from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Config

import allure

from pages.base_page import BasePage


class DzenPage(BasePage):
    def get_link_dzen(self):
        self.wait_and_find_element

