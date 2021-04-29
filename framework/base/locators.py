from selenium.webdriver.common.by import By
from selenium_wrapper.elements import Element
from selenium_wrapper.enums import LocatorsEnum


class MainPageLocators(LocatorsEnum):
    LOGIN_LINK = Element(By.CSS_SELECTOR, "#login_link", "Login link")


class LoginPageLocators(LocatorsEnum):
    LOGIN_LINK = Element(By.CSS_SELECTOR, "#login_link", "Login link")
    SIGN_UP_LOGIN = Element(By.CSS_SELECTOR, "#id_registration-email", "Registration login field")
    SIGN_UP_PSWD = Element(By.CSS_SELECTOR, "#id_registration-password1", "Registration password field")
    SIGN_UP_PSWD_CONFIRM = Element(By.CSS_SELECTOR, "#id_registration-password2", "Registration password confirm field")
    SIGN_IN_LOGIN = Element(By.CSS_SELECTOR, "#id_login-username", "Sign ip login field")
    SIGN_IN_PSWD = Element(By.CSS_SELECTOR, "#id_login-password", "Sign ip password field")


class BasketPageLocators(LocatorsEnum):
    ADD_TO_BASKET = Element(By.CSS_SELECTOR, ".btn-add-to-basket", "Add to basket button")
    MESSAGES = Element(By.XPATH, '//div[contains(@class,"alert alert-safe alert-noicon")][*]//strong', 'Messages about buying')
    PRICE = Element(By.CSS_SELECTOR, ".product_main > .price_color", "Book price")
    BOOK_NAME = Element(By.CSS_SELECTOR, ".product_main > h1", "Book name")
    CLEAR_BASKET_LABEL = Element(By.CSS_SELECTOR, "#content_inner", "Basket is clear label")


class MenuLocators(LocatorsEnum):
    GO_TO_BASKET = Element(By.XPATH, '//a[@href="/ru/basket/"][@class="btn btn-default"]', "Basket href")