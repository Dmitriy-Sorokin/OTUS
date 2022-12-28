import time
import allure
from home_task_page_object.page_object.adminka import Admin
from allure_commons.types import Severity


@allure.story("Story ST-229 Add element to the admin page")
@allure.title("Checked added elements in page")
@allure.description("Check all the items on the admin page as specified in the user story")
@allure.severity(severity_level=Severity.BLOCKER)
@allure.testcase("LINK_TO_THE_TEST_CASE")
def test_admin_check_element(browser):
    with allure.step("Step one. Checked verify element"):
        Admin(browser).check_elements()


@allure.feature("Feature ST-443 Name feature")
@allure.title("Checked errors to the admin page")
@allure.description("Check the case with the wrong data, check the errors on the page")
@allure.severity(severity_level=Severity.CRITICAL)
@allure.testcase("LINK_TO_THE_TEST_CASE")
def test_check_error(browser):
    with allure.step("Step two. Checked errors to the admin page"):
        Admin(browser).check_error("user", "bitnami1")


@allure.epic("Epic ST-554 Name epic")
@allure.title("Checked login")
@allure.description("Checking how the login works on the admin page")
@allure.severity(severity_level=Severity.NORMAL)
@allure.testcase("LINK_TO_THE_TEST_CASE")
def test_checked_login(browser):
    with allure.step("Step three. Login to the admin"):
        Admin(browser).login_in_adminka("user", "bitnami")


@allure.story("Story ST-856 Name story")
@allure.title("Checked element to the forgot page")
@allure.description("Checking the availability of elements as indicated in the story")
@allure.severity(severity_level=Severity.MINOR)
@allure.testcase("LINK_TO_THE_TEST_CASE")
def test_checked_elem_forgot_pass(browser):
    with allure.step("Step four. Checked elements to the forgot page "):
        Admin(browser).check_elem_at_page_forgot_password()


@allure.story("Story ST-553 Name epic")
@allure.title("Checked incorrect wrong data for input email")
@allure.description("Checked how the email input field will react to invalid data")
@allure.severity(severity_level=Severity.NORMAL)
@allure.testcase("LINK_TO_THE_TEST_CASE")
def test_input_incorrect_data_for_email(browser):
    with allure.step("Step fife. Checked input incorrect data for email"):
        Admin(browser).input_incorrect_data_for_email("asdfg@gmail.com")
