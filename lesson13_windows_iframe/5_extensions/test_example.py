import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from lesson13_windows_iframe.config import CHROMEDRIVER


@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_extension("ublock.crx")
    driver = webdriver.Chrome(service=Service(CHROMEDRIVER), options=options)
    driver.get("https://konflic.github.io/examples/")
    yield driver
    driver.close()


def test_disabled_button(browser):
    browser.get("https://demo.opencart.com/index.php?route=product/product&product_id=43")
    browser.find_element(By.ID, "button-cart").click()
    time.sleep(5)
