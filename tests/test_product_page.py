import pytest

from framework.base.pages_transfer import PageNamesEnum


@pytest.mark.skip
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    mainPage = browser.get_page(PageNamesEnum.productPage)
    mainPage.open()
    mainPage.go_to_basket_click()
    basketPage = browser.get_page(PageNamesEnum.basketPage)
    basketPage.should_be_clear()


@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    basketPage = browser.get_page(PageNamesEnum.basketPage, url=url)
    basketPage.open()
    basketPage.should_not_have_products()