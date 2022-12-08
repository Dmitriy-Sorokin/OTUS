import time

from home_task_page_object.page_object.adminka import Admin


def test_adminka(browser):
    Admin(browser).check_elements()
    time.sleep(2)
    Admin(browser).login_in_adminka("user", "bitnami")
    time.sleep(2)
    # browser.get(browser.url + "/admin/")
    # browser.find_element(*Admin.HEADING_PANEL)
    # browser.find_element(*Admin.INPUT_PASSWORD)
    # browser.find_element(*Admin.INPUT_USERNAME)
    # browser.find_element(*Admin.FORGOT_PASSWORD)
    # browser.find_element(*Admin.BTN_LOGIN)
    # time.sleep(2)
