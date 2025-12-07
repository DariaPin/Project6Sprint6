from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):
    def set_name_input(self,name):
        self.send_keys(OrderPageLocators.NAME_INPUT,name)

    def set_lastname_input(self, lastname):
        self.send_keys(OrderPageLocators.LASTNAME_INPUT,lastname)


    def set_adress_input(self, adress):
        self.send_keys(OrderPageLocators.ADRESS_INPUT, adress)

    def set_station_select(self,subway_name ):
        return [By.XPATH, f".//div[text()='{subway_name}']/parent::button"]

    def set_phone_input(self, phone):
        self.send_keys(OrderPageLocators.ADRESS_INPUT, phone)

    def click_order_button(self):
        self.wait_and_click(OrderPageLocators.NEXT_BUTTON)
    def previos_button_is_displayed(self):
        self.wait_and_find_element(OrderPageLocators.PREVIOUS_BUTTON)



