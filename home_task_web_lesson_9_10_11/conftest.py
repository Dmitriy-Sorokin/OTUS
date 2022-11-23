import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import Chrome, Firefox, Remote


def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "firefox"])
    parser.addoption("--url", action="store", default="http://10.48.67.16:8081")


# @pytest.fixture(scope="session")
# def url(request):
#     return request.config.getoption("--url")


@pytest.fixture
def browser(request):
    _browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")
    url = request.config.getoption("--url")

    driver = None

    if _browser == "chrome":
        options = webdriver.ChromeOptions()
        if maximized:
            options.headless = False
        driver = webdriver.Chrome(executable_path="c:\soft\drivers\chromedriver", options=options)
        driver.maximize_window()
        # driver = Chrome(executable_path=ChromeDriverManager().install())
    elif _browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.headless = True
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
        # driver = webdriver.Firefox(executable_path="c:\soft\drivers\geckodriver", driver.maximize_window())



    driver.get(url)
    driver.url = url

    # request.addfinalizer(driver.quit())

    return driver
