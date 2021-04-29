def test_guest_can_go_to_login_page(browser):
    login_page = browser.get_page("login")
    login_page.open()
    login_page.should_be_login_link()
    login_page.should_be_sign_in_form()
    login_page.should_be_sign_up_form()





