from framework.pages.main_page import MainPage
from framework.pages.login_page import LoginPage
from framework.pages.basket_page import BasketPage
from framework.pages.product_page import ProductPage
from selenium_wrapper.enums import PagesEnum


class PageNamesEnum(PagesEnum):
    mainPage = "main"
    loginPage = "login"
    basketPage = "basket"
    productPage = "product"


class Transfer:
    pages = {PageNamesEnum.mainPage.value: MainPage,
             PageNamesEnum.loginPage.value: LoginPage,
             PageNamesEnum.basketPage.value: BasketPage,
             PageNamesEnum.productPage.value: ProductPage}

    def set_browser(self, browser):
        self.browser = browser

    def get_page(self, str_page, **kwargs):
        if str_page is not str:
            str_page = str_page.value
        return self.pages[str_page](self.browser, **kwargs)

