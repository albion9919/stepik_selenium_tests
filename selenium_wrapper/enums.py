from enum import Enum
from selenium_wrapper.elements import Element


class LocatorsEnum(Enum):
    def __init__(self, element: Element):
        self.element = element


class PagesEnum(Enum):
    def __init__(self, page_class):
        self.page_class = page_class
