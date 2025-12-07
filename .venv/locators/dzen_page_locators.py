from selenium.webdriver.common.by import By

class DzenPageLocators:

    LOGO = (By.XPATH, "//button//span[text()='Войти']")
    LINK = "https://dzen.ru/?yredirect=true"