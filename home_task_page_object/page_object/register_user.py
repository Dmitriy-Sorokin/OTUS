from selenium.webdriver.common.by import By
from home_task_page_object.page_object.BasePage import BasePage
from random_word import RandomWords
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
    RB_YES = (By.CSS_SELECTOR, ".radio-inline input")
    RB_NO = (
        By.CSS_SELECTOR, "#content > form > fieldset:nth-child(3) > div > div > label:nth-child(2) > input[type=radio]")
    AC_CREATED = (By.CSS_SELECTOR, ".col-sm-9 h1")
    CONTINUE = (By.LINK_TEXT, "Continue")

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
        self._click(self.BTN_CONTINUE)
        alert_text = self.browser.find_element(*self.ALERT_DANGER).text
        expected_text = "Warning: You must agree to the Privacy Policy!"
        assert alert_text == expected_text
        time.sleep(1)

    def checked_input_not_correctly_data(self):
        random_words = RandomWords()
        self._click(self.MY_ACCOUNT)
        time.sleep(1)
        self._click(self.REG)
        time.sleep(1)
        self._element(self.FIRST_NAME).clear()
        self._element(self.FIRST_NAME).send_keys("first_name")
        self._element(self.LAST_NAME).clear()
        self._element(self.LAST_NAME).send_keys("last name")
        self._element(self.E_MAIL).clear()
        self._element(self.E_MAIL).send_keys(f"{random_words.get_random_word()}@email.com")
        self._element(self.PHONE).clear()
        self._element(self.PHONE).send_keys("1234455")
        self._element(self.PASS_INP).clear()
        self._element(self.PASS_INP).send_keys("zxcasd")
        self._element(self.PASS_CONF).clear()
        self._element(self.PASS_CONF).send_keys("zxcasd")
        self._click(self.RB_YES)
        self._click(self.RB_NO)
        self._click(self.P_POLICY)
        self._click(self.BTN_CONTINUE)
        text = self.browser.find_element(*self.AC_CREATED).text
        text_created = "Your Account Has Been Created!"
        assert text == text_created
        self._click(self.CONTINUE)
