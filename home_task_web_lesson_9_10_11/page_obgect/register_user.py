from selenium.webdriver.common.by import By


class Register:
    MY_ACCOUNT = (By.CSS_SELECTOR, "#top-links > ul > li.dropdown > a > span.caret")
    REG = (By.CSS_SELECTOR, "#top-links > ul > li.dropdown.open > ul > li:nth-child(1) > a")
    ELEMENT_BLOCK = (By.XPATH, "//*[@id='column-right']/div")  # 13 elements
    FIRST_NAME = (By.CSS_SELECTOR, "#input-firstname")
    LAST_NAME = (By.CSS_SELECTOR, "#input-lastname")
    E_MAIL = (By.CSS_SELECTOR, "#input-email")
    PHONE = (By.CSS_SELECTOR, "#input-telephone")
    PASS_INP = (By.CSS_SELECTOR, "#input-password")
    PASS_CONF = (By.CSS_SELECTOR, "#input-confirm")
    P_POLICY = (By.CSS_SELECTOR, "#content > form > div > div > input[type=checkbox]:nth-child(2)")
    BTN_CONTINUE = (By.CSS_SELECTOR, "#content > form > div > div > input.btn.btn-primary")
