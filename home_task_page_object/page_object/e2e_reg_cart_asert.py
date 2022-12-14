from selenium.webdriver.common.by import By
from home_task_page_object.page_object.BasePage import BasePage
import time


class PathUsers(BasePage):
    MY_ACCOUNT = (By.CSS_SELECTOR, ".dropdown")
    LOGIN = (By.LINK_TEXT, "Login")
    INPUT_EMAIL = (By.CSS_SELECTOR, "#input-email")  # dmitriyemail@gmail.com
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")  # 1234qwer
    BTN_LOGIN = (By.CSS_SELECTOR, ".btn-primary")
    TABLETS = (By.LINK_TEXT, "Tablets")
    TEXT_PRICE = (By.CSS_SELECTOR, "#content > div:nth-child(3) > div > div > div:nth-child(2) > div.caption > p.price")
    ADD_TO_CART = (By.CSS_SELECTOR, ".button-group button")
    SHOPPING_CART = (By.LINK_TEXT, "Shopping Cart")
    PRODUCT_NAME = (By.LINK_TEXT, "Samsung Galaxy Tab 10.1")
    UNIT_PRICE = (By.CSS_SELECTOR, "#content > form > div > table > tbody > tr > td:nth-child(5)")
    TOTAL_PRICE = (By.CSS_SELECTOR, "#content > form > div > table > tbody > tr > td:nth-child(6)")
    CONTINUE_SOP = (By.LINK_TEXT, "Continue Shopping")
    DD_CART = (By.CSS_SELECTOR, ".btn-inverse")
    BTN_DANGER = (By.CSS_SELECTOR, ".btn-danger")

    def e2epath(self, email, password):
        self._click(self.MY_ACCOUNT)
        self._click(self.LOGIN)
        self._element(self.INPUT_EMAIL).clear()
        self._element(self.INPUT_EMAIL).send_keys(email)
        self._element(self.INPUT_PASSWORD).clear()
        self._element(self.INPUT_PASSWORD).send_keys(password)
        self._click(self.LOGIN)
        self._click(self.TABLETS)
        self._click(self.ADD_TO_CART)
        self._click(self.SHOPPING_CART)


