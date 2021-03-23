from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import log, sin
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Browser:
    def __enter__(self):
        self.browser = webdriver.Chrome()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.browser.quit()

    def url(self, link):
        self.browser.get(link)

    def get(self, link):
        self.browser.get(link)

    def quit(self):
        self.browser.quit()

    def find(self, type, selector):
        if isinstance(type, str):
            return self.browser.find_element(self.get_type(type), selector)
        return self.browser.find_element(type, selector)

    def get_type(self, s):
        if s == "css":
            return By.CSS_SELECTOR
        if s == "xpath":
            return By.XPATH
        if s == "tag":
            return By.TAG_NAME
        if s == "class":
            return By.CLASS_NAME
        if s == "id":
          return By.ID
        if s == "name":
            return By.NAME

    def sleep(self, n):
        time.sleep(n)

    def wait(self, n):
        time.sleep(n)

    def get_attribute(self, element, s):
        element.get_attribute(s)

    def execute_script(self, s, el=None):
        if el is not None:
            self.browser.execute_script(s, el)
        self.browser.execute_script(s)

    def get_first_btn(self):
        return self.find("css", ".btn")

    def get_click_btn(self):
        self.find("css", ".btn").click()

    def switch_to_alert(self):
        return self.browser._switch_to.alert

    def alert_text(self):
        alert = self.browser._switch_to.alert
        t = alert.text
        alert.accept()
        return t

    def get_answer(self):
        return self.alert_text().split(":")[1]

    def accept_alert(self):
        self.switch_to_alert().accept()

    def get_int(self, type, s):
        return int(self.find(type, s).text)

    def compute(self, type, s):
        return str(log(abs(12*sin(self.get_int(type, s)))))

    def switch_to_window_new(self):
        self.browser.switch_to.window(self.browser.window_handles[1])

    def switch_to_window_start(self):
        self.browser.switch_to.window(self.browser.window_handles[0])

    def implicitly_wait(self):
        self.browser.implicitly_wait(5)

    def find_wait(self, type, selector, rule_s="visible", text=None, time_limit=5):
        if rule_s == "clickable":
            return WebDriverWait(self.browser, time_limit).until(
                EC.element_to_be_clickable((self.get_type(type), selector))
            )
        if rule_s == "text_present":
            return WebDriverWait(self.browser, time_limit).until(
                EC.text_to_be_present_in_element((self.get_type(type), selector), text_=text)
            )
        if rule_s == "visible":
            return WebDriverWait(self.browser, time_limit).until(
                EC.visibility_of(self.find(type, selector))
            )
        if rule_s == "presence":
            return WebDriverWait(self.browser, time_limit).until(
                EC.presence_of_element_located((self.get_type(type), selector))
            )

    def scroll_px(self,  px=100):
        return self.execute_script(f"return window.scrollBy(0, {px});")

    def scroll(self, type, selector, px=100):
        return self.execute_script("return arguments[0].scrollIntoView(true);", self.find(type, selector))




"""
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')
if os.path.isfile(file_path):
    os.remove(file_path)
file = open(file_path, "w")
file.write("Your text goes here")
file.close()
"""

#select = Select(b.find("id", "dropdown"))
#select.select_by_value(str(x))

# //*[@type='submit']   == .btn