import time

# Deprecated
from selenium.webdriver.common.by import By


def test_login_page(browser):
    browser.get(browser.url + "/admin")
    browser.find_element(value="input-username")
    browser.find_element(By.NAME, "password")
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    browser.find_element(By.LINK_TEXT, "Forgotten Password")
    browser.find_element(By.XPATH, "//*[text()='OpenCart']")
    time.sleep(5)  # Для демонстрации
