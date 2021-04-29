from framework.base.base_page import BasePage
from framework.base.locators import LoginPageLocators
from selenium_wrapper.elements import ElementWrapper


class LoginPage(BasePage):
    def __init__(self, browser, url="http://selenium1py.pythonanywhere.com/ru/accounts/login/", timeout=10):
        super().__init__(browser, url, timeout)
        self.LOGIN_LINK = ElementWrapper(self.browser, LoginPageLocators.LOGIN_LINK)
        self.SIGN_IN_LOGIN = ElementWrapper(self.browser, LoginPageLocators.SIGN_IN_LOGIN)
        self.SIGN_IN_PSWD = ElementWrapper(self.browser, LoginPageLocators.SIGN_IN_PSWD)
        self.SIGN_UP_LOGIN = ElementWrapper(self.browser, LoginPageLocators.SIGN_UP_LOGIN)
        self.SIGN_UP_PSWD = ElementWrapper(self.browser, LoginPageLocators.SIGN_UP_PSWD)
        self.SIGN_UP_PSWD_CONFIRM = ElementWrapper(self.browser, LoginPageLocators.SIGN_UP_PSWD_CONFIRM)

    def should_be_login_link(self):
        assert self.LOGIN_LINK.is_element_present(), \
            f"{self.LOGIN_LINK.element.description} is not presented"
        assert self.browser.url_contains("login"), \
            f"is not login url"

    def should_be_sign_in_form(self):
        assert self.SIGN_IN_LOGIN.is_element_present(), \
            f"{self.SIGN_IN_LOGIN.get_description()} is not presented"
        assert self.SIGN_IN_PSWD.is_element_present(), \
            f"{self.SIGN_IN_PSWD.get_description()} is not presented"

    def should_be_sign_up_form(self):
        assert self.SIGN_UP_LOGIN.is_element_present(), \
            f"{self.SIGN_UP_LOGIN.get_description()} is not presented"
        assert self.SIGN_IN_PSWD.is_element_present(), \
            f"{self.SIGN_UP_PSWD.get_description()} is not presented"
        assert self.SIGN_UP_PSWD_CONFIRM.is_element_present(), \
            f"{self.SIGN_UP_PSWD_CONFIRM.get_description()} is not presented"


