from home_task_page_object.page_object.e2e_reg_cart_asert import PathUsers


def test_path_add_cart(browser):
    PathUsers(browser).e2epath("dmitriyemail@gmail.com", "1234qwer")
