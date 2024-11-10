import pytest
from selenium import webdriver

@pytest.fixture
def setup():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("")
    yield driver
    driver.quit()

    