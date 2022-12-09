from selenium.webdriver.common.by import By
from home_task_page_object.page_object.BasePage import BasePage
import time


class Register(BasePage):
    MY_ACCOUNT = (By.CSS_SELECTOR, ".dropdown")
    REG = (By.LINK_TEXT, "Register")
    ELEMENT_BLOCK = (By.CSS_SELECTOR, ".list-group a")  # 13 elements
    FIRST_NAME = (By.CSS_SELECTOR, "#input-firstname")
    LAST_NAME = (By.CSS_SELECTOR, "#input-lastname")
    E_MAIL = (By.CSS_SELECTOR, "#input-email")
    PHONE = (By.CSS_SELECTOR, "#input-telephone")
    PASS_INP = (By.CSS_SELECTOR, "#input-password")
    PASS_CONF = (By.CSS_SELECTOR, "#input-confirm")
    P_POLICY = (By.CSS_SELECTOR, "#content > form > div > div > input[type=checkbox]:nth-child(2)")
    BTN_CONTINUE = (By.CSS_SELECTOR, "#content > form > div > div > input.btn.btn-primary")
    ALERT_DANGER = (By.CSS_SELECTOR, ".alert-danger")

    def check_element_reg_user(self):
        self._verify_element_present(self.MY_ACCOUNT).click()
        time.sleep(1)
        self._verify_element_present(self.REG).click()
        time.sleep(1)
        len_block = self.browser.find_elements(*self.ELEMENT_BLOCK)
        assert len(len_block) == 13
        self._verify_element_present(self.FIRST_NAME)
        self._verify_element_present(self.LAST_NAME)
        self._verify_element_present(self.E_MAIL)
        self._verify_element_present(self.PHONE)
        self._verify_element_present(self.PASS_INP)
        self._verify_element_present(self.PASS_CONF)
        self._verify_element_present(self.P_POLICY)
        self._verify_element_present(self.BTN_CONTINUE).click()
        alert_text = self.browser.find_element(*self.ALERT_DANGER).text
        expected_text = "Warning: You must agree to the Privacy Policy!"
        assert alert_text == expected_text
        time.sleep(1)
