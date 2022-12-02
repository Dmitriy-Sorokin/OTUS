import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import Chrome, Firefox, Remote
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="https://demo.opencart.com/")
    parser.addoption("--drivers", action="store", default=os.path.expanduser("c:\soft\drivers"))


@pytest.fixture
def browser(request):
    # Сбор параметров для запуска pytest
    _browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    drivers = request.config.getoption("--drivers")

    if _browser == "chrome":
        # В selenium 4 рекомендуют использование такого подхода
        service = ChromiumService(executable_path=drivers + "\chromedriver")
        driver = Chrome(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif _browser == "firefox":
        service = FFService(executable_path=drivers + "\geckodriver")
        #driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)

    driver.maximize_window()

    request.addfinalizer(driver.close)

    driver.get(url)
    driver.url = url

    return driver