from selenium.webdriver.common.by import By


class Homepage:
    SEARCH_INPUT = (By.CSS_SELECTOR, "#search > input")
    SEARCH = (By.CSS_SELECTOR, "#search > span > button")
    PHONE = (By.XPATH, "//*[@id='top-links']/ul/li[1]/a/i")
    MY_ACCOUNT = (By.CSS_SELECTOR, "#top-links > ul > li.dropdown > a")
