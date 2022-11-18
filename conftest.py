import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome, Firefox, Remote


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
        # driver = webdriver.Chrome(executable_path="c:\soft\drivers\chromedriver")
        driver = Chrome(executable_path=ChromeDriverManager().install())
    elif _browser == "firefox":
        driver = webdriver.Firefox(executable_path="c:\soft\drivers\geckodriver")

    if maximized:
        driver.maximize_window()

    def final():
        driver.quit()

    request.addfinalizer(final)

    return driver
