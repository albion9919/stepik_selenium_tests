from selenium_wrapper.elements import ElementWrapper, ElementList
from framework.base.base_page import BasePage
from framework.base.locators import BasketPageLocators


class BasketPage(BasePage):
    def __init__(self, browser, url=None, timeout=10):
        super().__init__(browser, url, timeout)
        self.add_to_basket_btn = ElementWrapper(self.browser, BasketPageLocators.ADD_TO_BASKET)
        self.messages = ElementList(self.browser, BasketPageLocators.MESSAGES)
        self.book_name = ElementWrapper(self.browser, BasketPageLocators.BOOK_NAME)
        self.price = ElementWrapper(self.browser, BasketPageLocators.PRICE)
        self.clear_basket_label = ElementWrapper(self.browser, BasketPageLocators.CLEAR_BASKET_LABEL)

    def add_to_basket(self):
        self.add_to_basket_btn.find().click()

    def should_check_buying(self):
        assert f"{self.book_name.text}" == self.messages.get_element(0).text, \
            f"{self.book_name.get_description()} is incorrect"
        assert f"{self.price.text}" == self.messages.get_element(2).text, \
            f"{self.price.get_description()} is incorrect"

    def should_not_have_products(self):
        self.messages.is_not_element_present()

    def should_not_have_products_dissapeared(self):
        self.messages.is_disappeared()

    def should_be_clear(self):
        self.clear_basket_label.is_element_present()
        assert self.clear_basket_label.text == "Ваша корзина пуста Продолжить покупки"
"""
Coders at Work был добавлен в вашу корзину.
×
Ваша корзина удовлетворяет условиям предложения Deferred benefit offer.
×
Стоимость корзины теперь составляет 19,99 £
"""


# //div[@class="alert alert-safe alert-noicon alert-success  fade in"][]/div/strong



