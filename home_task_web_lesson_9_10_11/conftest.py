import pytest

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "firefox"])
    parser.addoption("--url", action="store", default="http://10.48.67.16:8081")


@pytest.fixture
def browser(request):
    _browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")
    url = request.config.getoption("--url")

    if _browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.headless = True
        driver = webdriver.Chrome(executable_path="c:\soft\drivers\chromedriver", options=options)
        driver.maximize_window()
    elif _browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.headless = True
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
        driver.maximize_window()
    else:
        raise Exception("Driver not supported")

    request.addfinalizer(driver.quit)

    driver.get(url)
    driver.url = url

    return driver
