import math
from selenium.common.exceptions import NoAlertPresentException
from framework.base.locators import MenuLocators
from selenium_wrapper.elements import ElementWrapper


class BasePage:
    def __init__(self, browser, url=None, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        self.go_to_basket_btn = ElementWrapper(self.browser, MenuLocators.GO_TO_BASKET)

    def open(self):
        self.browser.get(self.url)

    def solve_quiz_and_get_code(self):
        alert = self.browser.driver.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.driver.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def go_to_basket_click(self):
        self.go_to_basket_btn.click()
