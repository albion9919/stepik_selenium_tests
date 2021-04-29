from selenium import webdriver
import time
from math import log, sin


class Browser:
    def __init__(self, transfer=None):
        self.driver = webdriver.Chrome()
        self.transfer = transfer
        if self.transfer is not None:
            self.transfer.set_browser(self)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()

    def get_page(self, str_page, **kwargs):
        if self.transfer is not None:
            return self.transfer.get_page(str_page, **kwargs)
        else:
            raise Exception("No any transfer")

    def url(self, link):
        self.driver.get(link)

    def get(self, link):
        self.driver.get(link)

    def quit(self):
        self.driver.quit()

    def wait(self, n):
        time.sleep(n)

    def execute_script(self, script, element=None):
        if element is not None:
            self.driver.execute_script(script, element)
        self.driver.execute_script(script)

    def switch_to_alert(self):
        return self.driver._switch_to.alert

    def alert_text(self):
        alert = self.driver._switch_to.alert
        t = alert.text
        alert.accept()
        return t

    def accept_alert(self):
        self.switch_to_alert().accept()

    def switch_to_window_new(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def switch_to_window_start(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    def implicitly_wait(self, timeout=10):
        self.driver.implicitly_wait(timeout)

    def scroll_px(self, px=100):
        return self.execute_script(f"return window.scrollBy(0, {px});")

    def scroll(self, element):
        return self.execute_script("return arguments[0].scrollIntoView(true);", element.find())

    def current_url(self):
        return self.driver.current_url

    def url_contains(self, strx):
        return strx in self.driver.current_url


class Hepler(Browser):
    def get_int(self, element):
        return int(element.find().text)

    def compute(self, element):
        return str(log(abs(12 * sin(self.get_int(element)))))

    def get_answer(self):
        return self.alert_text().split(":")[1]

