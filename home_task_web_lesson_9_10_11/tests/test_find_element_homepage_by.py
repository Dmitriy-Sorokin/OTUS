import time
from home_task_web_lesson_9_10_11.page_obgect.homepage import Homepage


def test_find_element_homepage(browser):
    time.sleep(2)
    browser.find_element(*Homepage.PHONE)
    browser.find_element(*Homepage.SEARCH_INPUT)
    browser.find_element(*Homepage.SEARCH)
    browser.find_element(*Homepage.MY_ACCOUNT)
    canon = browser.find_element(*Homepage.CANON)
    canon.click()
    time.sleep(2)
