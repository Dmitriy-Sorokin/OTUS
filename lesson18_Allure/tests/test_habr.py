from lesson18_Allure.page_objects.HabrObject import HabrObject


def test_post_open(driver):
    page = HabrObject(driver)
    page.open()
    page.click_search()
    page.search('Python')
    page.read_more()
    page.is_present(page.POST_BODY)


def test_hubs_open(driver):
    page = HabrObject(driver)
    page.open()
    page.click_search()
    page.search('Python')
    page.select_hubs()
    page.is_present(page.HUBS)
