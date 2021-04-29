from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ElementAbstract:
    def __init__(self, browser, element):
        self.element = element.value
        self.web_element = None
        self.driver = browser.driver

    def find_wait(self, rule_s="visible", text=None, time_limit=5):
        if rule_s == "clickable":
            return WebDriverWait(self.driver, time_limit).until(
                EC.element_to_be_clickable(self.element.get_element())
            )
        if rule_s == "text_present":
            return WebDriverWait(self.driver, time_limit).until(
                EC.text_to_be_present_in_element(self.element.get_element(), text_=text)
            )
        if rule_s == "visible":
            return WebDriverWait(self.driver, time_limit).until(
                EC.visibility_of(self.driver.find(element=self))
            )
        if rule_s == "presence":
            return WebDriverWait(self.driver, time_limit).until(
                EC.presence_of_element_located(self.element.get_element())
            )

    def is_element_present(self):
        try:
            self.find()
        except NoSuchElementException:
            return False
        return True

    def find(self):
        pass

    def get_description(self):
        return self.element.description

    def is_not_element_present(self, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(self.element.get_element()))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, timeout=5):
        try:
            WebDriverWait(self.driver, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located(self.element.get_element()))
        except TimeoutException:
            return False
        return True


class ElementWrapper(ElementAbstract):
    def get_attribute(self,  s):
        self.find()
        return self.web_element.get_attribute(s)

    @property
    def text(self):
        self.find()
        return self.web_element.text

    def find(self):
        self.web_element = self.driver.find_element(*self.element.get_element())
        return self.web_element

    def click(self):
        self.find()
        self.web_element.click()


class ElementList(ElementAbstract):
    def find(self):
        self.web_element = self.driver.find_elements(*self.element.get_element())
        return self.web_element

    def get_element(self, number: int):
        self.find()
        return self.web_element[number]


class Element:
    def __init__(self, locator_type, locator, description=None):
        self.locator_type = self.__get_type(locator_type)
        self.locator = locator
        self.description = description

    def __get_type(self, s):
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
        return s

    def get_element(self):
        return self.locator_type, self.locator
