from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    def question_click(self,number):
        self.wait_and_find_element(MainPageLocators.faq_question_button(number)).click()

    def answer_text(self, number_answer):
        answer = self.wait_and_find_element(MainPageLocators.faq_answer_button(number_answer))
        return answer.text







