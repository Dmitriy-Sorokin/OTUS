import time
from home_task_web_lesson_9_10_11.page_obgect.register_user import Register


def test_reg_user(browser):
    acc = browser.find_element(*Register.MY_ACCOUNT)
    acc.click()
    time.sleep(2)
    reg = browser.find_element(*Register.REG)
    reg.click()
    browser.find_elements(*Register.ELEMENT_BLOCK)
    browser.find_element(*Register.FIRST_NAME)
    browser.find_element(*Register.LAST_NAME)
    browser.find_element(*Register.E_MAIL)
    browser.find_element(*Register.PHONE)
    browser.find_element(*Register.PASS_INP)
    browser.find_element(*Register.PASS_CONF)
    browser.find_element(*Register.P_POLICY)
    browser.find_element(*Register.BTN_CONTINUE)
    time.sleep(2)
