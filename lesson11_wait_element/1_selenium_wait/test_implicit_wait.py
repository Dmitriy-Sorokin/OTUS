from selenium.webdriver.common.by import By
import time

def test_check_header(browser):
    browser.implicitly_wait(5)
    browser.get("https://konflic.github.io/examples/pages/slowlyloading.html")
    browser.find_element(By.CSS_SELECTOR, "#header")
    time.sleep(3)
