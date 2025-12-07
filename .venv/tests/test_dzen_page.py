from data import OrderAnswer
from pages.main_page import MainPage
import pytest
class TestDzenPage:

        dzen_page = DzenPage(driver)
        title = dzen_page.get_profile_title(DzenPageTestData.NAME)

        # Assert
        assert title.text == LoginPageTestData.NAME