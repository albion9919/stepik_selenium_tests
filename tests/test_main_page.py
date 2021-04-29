import pytest

from framework.base.pages_transfer import PageNamesEnum


def test_guest_can_go_to_login_page(browser):
    main_page = browser.get_page("main")
    main_page.open()
    login_page = main_page.go_to_login_page()
    login_page.should_be_login_link()


@pytest.mark.skip
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    mainPage = browser.get_page(PageNamesEnum.mainPage)
    mainPage.open()
    mainPage.go_to_basket_click()
    basketPage = browser.get_page(PageNamesEnum.basketPage)
    basketPage.should_be_clear()