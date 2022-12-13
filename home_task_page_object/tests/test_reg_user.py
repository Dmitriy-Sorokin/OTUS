import time
from home_task_page_object.page_object.register_user import Register


def test_reg_user(browser):
    Register(browser).check_element_reg_user()
    # acc = browser.find_element(*Register.MY_ACCOUNT)
    # acc.click()
    # time.sleep(2)
    # reg = WebDriverWait(browser, 3).until(EC.visibility_of_element_located(Register.REG))
    # reg.click()
    # elem = browser.find_elements(*Register.ELEMENT_BLOCK)
    # assert len(elem) == 13
    # browser.find_element(*Register.FIRST_NAME)
    # browser.find_element(*Register.LAST_NAME)
    # browser.find_element(*Register.E_MAIL)
    # browser.find_element(*Register.PHONE)
    # browser.find_element(*Register.PASS_INP)
    # browser.find_element(*Register.PASS_CONF)
    # browser.find_element(*Register.P_POLICY)
    # WebDriverWait(browser, 3).until(EC.element_to_be_clickable(Register.BTN_CONTINUE))
    # time.sleep(2)
