from selenium_wrapper.elements import ElementWrapper
from framework.base.base_page import BasePage
from framework.base.locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, browser, url="http://selenium1py.pythonanywhere.com/", timeout=10):
        super().__init__(browser, url, timeout)
        self.login_link = ElementWrapper(self.browser, MainPageLocators.LOGIN_LINK)

    def go_to_login_page(self):
        self.login_link.find().click()
        return self.browser.get_page("login")




