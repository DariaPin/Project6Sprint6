from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.order_page import OrderPage
from data import OrderPageTestData


class TestOrderPage:
   def test_correct_fill_in(self, driver):
       order_page=OrderPage(driver)
       order_page.set_name_input(OrderPageTestData.NAME)
       order_page.set_lastname_input(OrderPageTestData.LAST_NAME)
       order_page.set_phone_input(OrderPageTestData.PHONE)
       order_page.set_adress_input(OrderPageTestData.ADRESS)
       order_page.set_station_select(OrderPageTestData.STATION)

