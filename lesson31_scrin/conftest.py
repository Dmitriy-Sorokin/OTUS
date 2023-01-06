import os
import allure
import pytest

from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from .config import BASE_URL
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--mobile", action="store_true", help="test mobile emulation")
    parser.addoption("--prod", action="store", default="https://konflic.github.io/examples/opencart/prod.html")
    parser.addoption("--stage", action="store", choices=["branch", "staging"], default="branch")
    parser.addoption("--executor", action="store", default="192.168.0.108")


@pytest.fixture(scope="session")
def browser(request):
    browser = request.config.getoption("--browser")
    mobile = request.config.getoption("--mobile")
    prod_url = request.config.getoption("--prod")
    executor = request.config.getoption("--executor")
    stage_url = f"{BASE_URL}/{request.config.getoption('--stage')}.html"

    capabilities = {
        "browserName": browser,
        "screenResolution": "1920x1080",
        "selenoid:options": {
            "enableVNC": True
        },
        "timeZone": "Europe/Moscow",
        "goog:chromeOptions": {}
    }

    if mobile:
        capabilities["browserName"] = "chrome"
        capabilities["goog:chromeOptions"]["mobileEmulation"] = {"deviceName": "iPhone 5/SE"}

    if browser == "firefox":
        # driver = webdriver.Chrome(service=Service("c:\soft\drivers\chromedriver"))
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    else:
        driver = webdriver.Remote(
            command_executor=f"http://{executor}:4444/wd/hub",
            desired_capabilities=capabilities
        )

    driver.stag_url, driver.prod_url = stage_url, prod_url

    allure.attach(
        name="config",
        body=f"'stag': {stage_url}\n'prod': {prod_url}",
        attachment_type=allure.attachment_type.TEXT
    )

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return driver
