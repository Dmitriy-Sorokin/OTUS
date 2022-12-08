from selenium.webdriver.common.by import By


class ProductCart:
    ADD_TO_CART = (By.CSS_SELECTOR, "#button-cart")
    QUANTITY = (By.CSS_SELECTOR, "#input-quantity")
    ADD_WISH_LIST = (By.CSS_SELECTOR, "#content > div > div.col-sm-4 > div.btn-group > button:nth-child(1)")
    COMPARE_THIS_PRODUCT = (By.CSS_SELECTOR, "#content > div > div.col-sm-4 > div.btn-group > button:nth-child(2)")
    COST = (By.CSS_SELECTOR, "#content > div > div.col-sm-4 > ul:nth-child(4) > li:nth-child(1) > h2")
    NAME_PRODUCT = (By.XPATH, "//*[@id='content']/div/div[2]/h1")