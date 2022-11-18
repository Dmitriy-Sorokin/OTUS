import time


def test_first(browser, url):
    browser.get(url)
    assert browser.title == "Your Store"
    time.sleep(5)

