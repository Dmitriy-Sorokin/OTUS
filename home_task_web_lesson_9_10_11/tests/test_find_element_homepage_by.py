import time
from home_task_web_lesson_9_10_11.page_obgect.homepage import Homepage


def test_find_element_homepage(browser):
    time.sleep(2)
    browser.find_element(*Homepage.PHONE)
    time.sleep(2)
