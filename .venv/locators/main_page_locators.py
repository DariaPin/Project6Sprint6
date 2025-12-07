from selenium.webdriver.common.by import By

class MainPageLocators:

    SKOLKO_ETO_STOIT = (By.XPATH, "//div[id='accordion__heading-0']")
    HOCHU_SRAZU_NESKOLKO = (By.XPATH, "//div[@id='accordion__heading-1']")
    KAK_RASSCHITIVAETSYA_VREMYA = (By.XPATH, "//div[@id='accordion__heading-2']")
    MOZNO_LI_ZAKAZAT_NA_SEGODNYA = (By.XPATH, "//div[@id='accordion__heading-3']")
    MOZNO_LI_PRODLIT = (By.XPATH, "//div[@id='accordion__heading-4']")
    VI_PIVOZITE_ZARYADKY = (By.XPATH,"//div[@id='accordion__heading-5']")
    MOZNO_LI_OTMENIT = (By.XPATH, "//div[@id='accordion__heading-6']")
    YA_ZIVU_ZA_MKADOM = (By.XPATH, "//div[@id='accordion__heading-7]")

    DZEN_LOGO = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")

    @staticmethod
    def faq_question_button(question_number):
        """Возвращает локатор кнопки с вопросом FAQ (нумерация сверху вниз)"""
        return [By.XPATH, f".//div[@class='accordion__button' and @id='accordion__heading-{question_number}']"]

    def faq_answer_button(answer_number):
        return [By.XPATH, f".//div[@class='accordion__button' and @id = 'accordion__panel-{answer_number}']"]

