import time

from home_task_page_object.page_object.adminka import Admin


def test_adminka(browser):
    Admin(browser).check_elements()
    time.sleep(1)
    Admin(browser).check_error("user", "bitnami1")
    #Admin(browser).login_in_adminka("user", "bitnami")
    time.sleep(1)

