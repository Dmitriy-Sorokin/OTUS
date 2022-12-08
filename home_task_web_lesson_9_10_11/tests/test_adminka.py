import time

from home_task_web_lesson_9_10_11.page_obgect.adminka import Admin


def test_adminka(browser):
    browser.get(browser.url + "/admin/")
    browser.find_element(*Admin.HEADING_PANEL)
    browser.find_element(*Admin.INPUT_PASSWORD)
    browser.find_element(*Admin.INPUT_USERNAME)
    browser.find_element(*Admin.FORGOT_PASSWORD)
    browser.find_element(*Admin.BTN_LOGIN)
    time.sleep(2)
