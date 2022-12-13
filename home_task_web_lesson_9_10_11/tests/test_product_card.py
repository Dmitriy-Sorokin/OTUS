import time
from home_task_web_lesson_9_10_11.page_object.product_card import ProductCart


def test_find_element_product_card(browser):
    browser.get(browser.url + "/tablet/samsung-galaxy-tab-10-1")
    browser.find_element(*ProductCart.NAME_PRODUCT)
    browser.find_element(*ProductCart.ADD_TO_CART)
    browser.find_element(*ProductCart.COMPARE_THIS_PRODUCT)
    browser.find_element(*ProductCart.COST)
    browser.find_element(*ProductCart.ADD_WISH_LIST)
    browser.find_element(*ProductCart.QUANTITY)
