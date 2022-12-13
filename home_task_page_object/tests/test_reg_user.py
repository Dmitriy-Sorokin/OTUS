import time
from home_task_page_object.page_object.register_user import Register


def test_reg_user(browser):
    # Register(browser).check_element_reg_user()
    time.sleep(1)
    Register(browser).checked_input_not_correctly_data()
    time.sleep(1)
