from selenium.webdriver.common.by import By


class Admin:
    INPUT_USERNAME = (By.CSS_SELECTOR, "#input-username")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    FORGOT_PASSWORD = (By.XPATH, "//*[@id='content']/div/div/div/div/div[2]/form/div[2]/span/a")
    BTN_LOGIN = (By.CSS_SELECTOR, "#content > div > div > div > div > div.panel-body > form > div.text-right > button")
    HEADING_PANEL = (By.CSS_SELECTOR, "#content > div > div > div > div > div.panel-heading > h1")
