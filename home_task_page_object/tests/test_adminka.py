import time

from home_task_page_object.page_object.adminka import Admin


def test_adminka(browser):
    """
    Test page (admin):
    Checking the presence of the necessary elements on the page
    Login to the admin panel
    Check email for validity
    The time slips are for illustrative purposes
    """
    Admin(browser).check_elements()
    time.sleep(1)
    Admin(browser).check_error("user", "bitnami1")
    time.sleep(1)
    Admin(browser).login_in_adminka("user", "bitnami")
    time.sleep(1)
    Admin(browser).check_elem_at_page_forgot_password()
    time.sleep(1)
    Admin(browser).input_incorrect_data_for_email("asdfg@gmail.com")
    time.sleep(1)
