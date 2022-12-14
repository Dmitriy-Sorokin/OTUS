import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import Chrome, Firefox, Remote
from selenium.webdriver.chrome.service import Service

'''Lesson9_Selenium'''


def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "firefox"])
    parser.addoption("--url", action="store", default="https://demo.opencart.com/")


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request):
    _browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")

    driver = None

    if _browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.headless = True
        # driver = webdriver.Chrome(executable_path="c:\soft\drivers\chromedriver", driver.maximize_window())
        driver = Chrome(service=Service(ChromeDriverManager().install()), options=options)
    elif _browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.headless = True
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
        # driver = webdriver.Firefox(executable_path="c:\soft\drivers\geckodriver")

    if maximized:
        driver.maximize_window()

    def final():
        driver.quit()

    request.addfinalizer(final)

    return driver
