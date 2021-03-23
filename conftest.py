import pytest
from module import Browser
@pytest.fixture(scope="function")
def browser():
    with Browser() as b:
        yield b