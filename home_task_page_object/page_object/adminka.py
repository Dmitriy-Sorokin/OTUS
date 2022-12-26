from selenium.webdriver.common.by import By
import time
from home_task_page_object.page_object.BasePage import BasePage


class Admin(BasePage):
    INPUT_USERNAME = (By.CSS_SELECTOR, "#input-username")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    FORGOT_PASSWORD = (By.XPATH, "//*[@id='content']/div/div/div/div/div[2]/form/div[2]/span/a")
    BTN_LOGIN = (By.CSS_SELECTOR, "#content > div > div > div > div > div.panel-body > form > div.text-right > button")
    HEADING_PANEL = (By.CSS_SELECTOR, "#content > div > div > div > div > div.panel-heading > h1")
    ERROR_TEXT = (By.XPATH, "/html/body/div/div/div/div/div/div/div[2]/div")
    CLOSE_ALERT = (By.CSS_SELECTOR, "#content > div > div > div > div > div.panel-body > div > button")
    PANEL_FORGOT_PASSWORD = (By.CSS_SELECTOR, ".panel-title")
    LABEL_EMAIL = (By.CSS_SELECTOR, "#content > div > div > div > div > div.panel-body > form > div.form-group > label")
    INPUT_EMAIL = (By.CSS_SELECTOR, ".form-control")
    RESET_BTN = (By.CSS_SELECTOR, ".btn-primary")
    ALERT_WARNING = (By.CSS_SELECTOR, ".alert-danger")
    CLOSE_ALERT_WARNING = (By.CSS_SELECTOR, ".close")
    CANSEL_BTN = (By.CSS_SELECTOR, ".btn-default")
    LINK_FORGOT = (By.LINK_TEXT, "Forgotten Password")

    def check_elements(self):
        time.sleep(2)
        self.get_param_url("/admin/")
        self._verify_element_present(self.INPUT_USERNAME)
        self._verify_element_present(self.INPUT_PASSWORD)
        self._verify_element_present(self.FORGOT_PASSWORD)
        self._verify_element_present(self.BTN_LOGIN)
        self._verify_element_present(self.HEADING_PANEL)

    def check_error(self, username, password):
        time.sleep(2)
        self.get_param_url("/admin/")
        self._element(self.INPUT_USERNAME).send_keys(username)
        self._element(self.INPUT_PASSWORD).send_keys(password)
        self._click(self.BTN_LOGIN)
        error = self.browser.find_element(*self.ERROR_TEXT).text
        text = str(error.replace("×", ""))[0:-1]
        assert text == str("No match for Username and/or Password.")
        self._click(self.CLOSE_ALERT)

    def login_in_adminka(self, username, password):
        self.get_param_url("/admin/")
        self._element(self.INPUT_USERNAME).clear()
        self._element(self.INPUT_USERNAME).send_keys(username)
        self._element(self.INPUT_PASSWORD).clear()
        self._element(self.INPUT_PASSWORD).send_keys(password)
        self._click(self.BTN_LOGIN)

    def check_elem_at_page_forgot_password(self):
        self.get_param_url("/admin/")
        self._click(self.LINK_FORGOT)
        self._verify_element_present(self.PANEL_FORGOT_PASSWORD)
        self._verify_element_present(self.LABEL_EMAIL)
        self._verify_element_present(self.INPUT_EMAIL)
        self._verify_element_present(self.RESET_BTN)
        self._verify_element_present(self.CANSEL_BTN)

    def input_incorrect_data_for_email(self, email):
        self.get_param_url("/admin/")
        self._click(self.LINK_FORGOT)
        self._element(self.INPUT_EMAIL).clear()
        self._element(self.INPUT_EMAIL).send_keys(email)
        self._click(self.RESET_BTN)
        text_warning = self.browser.find_element(*self.ALERT_WARNING).text
        text = str(text_warning.replace("×", ""))[0:-1]
        error_text = "Warning: The E-Mail Address was not found in our records, please try again!"
        self._click(self.CLOSE_ALERT_WARNING)
        assert text == error_text

