import pytest
from framework.base.pages_transfer import PageNamesEnum
product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]


def main_test(browser, url):
    basketPage = browser.get_page(PageNamesEnum.basketPage, url=url)
    basketPage.open()
    basketPage.add_to_basket()
    basketPage.solve_quiz_and_get_code()
    basketPage.should_check_buying()
    return basketPage


@pytest.mark.parametrize('link', urls)
@pytest.mark.skip
def test_guest_can_add_product_to_basket_singular(browser, link):
    main_test(browser, link)


@pytest.mark.skip
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    basketPage = main_test(browser, url)
    basketPage.should_be_success_negative()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    basketPage = main_test(browser, url)
    basketPage.should_not_have_products_dissapeared()






