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
        # assert text == str(
        #     "Warning: Your account has exceeded allowed number of login attempts. Please try again in 1 hour or reset password.")
        self._click(self.CLOSE_ALERT)


    def login_in_adminka(self, username, password):
        self.get_param_url("/admin/")
        self._element(self.INPUT_USERNAME).send_keys(username)
        self._element(self.INPUT_PASSWORD).send_keys(password)
        self._click(self.BTN_LOGIN)
