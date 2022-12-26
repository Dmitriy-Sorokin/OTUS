import time
from home_task_page_object.page_object.register_user import Register
import allure


@allure.title("Checked register user")
@allure.description("Verify elements in page registration user")
def test_checked_element(browser):
    Register(browser).check_element_reg_user()
    time.sleep(1)


@allure.title("Checked not correctly data")
@allure.description(
    "Check that the fields are filled in and that the buttons work,"
    " and go through the full business path to register the user.")
def test_input_not_correctly_deta(browser):
    Register(browser).checked_input_not_correctly_data()
    time.sleep(1)
