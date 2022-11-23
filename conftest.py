# import pytest
# import os
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromiumService
# from selenium.webdriver.firefox.service import Service as FFService
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver import Chrome, Firefox, Remote
# from selenium.webdriver.chrome.service import Service
#
# '''Lesson9_Selenium'''
# def pytest_addoption(parser):
#     parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
#     parser.addoption("--headless", action="store_true", help="Run headless")
#     parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "firefox"])
#     parser.addoption("--url", action="store", default="https://demo.opencart.com/")
#
#
# @pytest.fixture(scope="session")
# def url(request):
#     return request.config.getoption("--url")
#
#
# @pytest.fixture
# def browser(request):
#     _browser = request.config.getoption("--browser")
#     headless = request.config.getoption("--headless")
#     maximized = request.config.getoption("--maximized")
#
#     driver = None
#
#     if _browser == "chrome":
#         options = webdriver.ChromeOptions()
#         if headless:
#             options.headless = True
#         # driver = webdriver.Chrome(executable_path="c:\soft\drivers\chromedriver", driver.maximize_window())
#         driver = Chrome(executable_path=ChromeDriverManager().install(), options=options)
#     elif _browser == "firefox":
#         options = webdriver.FirefoxOptions()
#         if headless:
#             options.headless = True
#         driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
#         #driver = webdriver.Firefox(executable_path="c:\soft\drivers\geckodriver")
#
#     if maximized:
#         driver.maximize_window()
#
#     def final():
#         driver.quit()
#
#     request.addfinalizer(final)
#
#     return driver

# '''lesson10_element_search'''
#
#
# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="chrome")
#     parser.addoption("--url", action="store", default="https://demo.opencart.com/")
#     parser.addoption("--drivers", action="store", default=os.path.expanduser("c:\soft\drivers"))
#
#
# @pytest.fixture
# def browser(request):
#     # Сбор параметров для запуска pytest
#     _browser = request.config.getoption("--browser")
#     url = request.config.getoption("--url")
#     drivers = request.config.getoption("--drivers")
#
#     if _browser == "chrome":
#         # В selenium 4 рекомендуют использование такого подхода
#         service = ChromiumService(executable_path=drivers + "\chromedriver")
#         #driver = Chrome(executable_path=ChromeDriverManager().install())
#         driver = webdriver.Chrome(service=service)
#     # elif _browser == "firefox":
#     #     service = FFService(executable_path=drivers + "\geckodriver")
#     #     #driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#     #     driver = webdriver.Firefox(service=service)
#
#     driver.maximize_window()
#
#     request.addfinalizer(driver.close)
#
#     driver.get(url)
#     driver.url = url
#
#     return driver

# '''lesson 11 wait elements'''
#
# def pytest_addoption(parser):
#     parser.addoption("--browser", default="chrome")
#     parser.addoption("--drivers", default=os.path.expanduser("c:\soft\drivers"))
#
#
# @pytest.fixture
# def browser(request):
#     browser = request.config.getoption("--browser")
#     drivers = request.config.getoption("--drivers")
#
#     if browser == "chrome":
#         service = Service(executable_path=os.path.join(drivers, "chromedriver"))
#         driver = webdriver.Chrome(service=service)
#     elif browser == "firefox":
#         driver = webdriver.Firefox(executable_path=os.path.join(drivers, "geckodriver"))
#     else:
#         raise Exception("Driver not supported")
#
#     request.addfinalizer(driver.quit)
#
#     return driver
