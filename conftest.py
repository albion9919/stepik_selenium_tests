import pytest
from selenium_wrapper.module import Browser
from framework.base.pages_transfer import Transfer


@pytest.fixture(scope="function")
def browser():
    transfer = Transfer()
    with Browser(transfer=transfer) as __browser:
        yield __browser

