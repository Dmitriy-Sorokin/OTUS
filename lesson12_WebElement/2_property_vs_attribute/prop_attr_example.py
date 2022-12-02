from selenium import webdriver
from lesson12_WebElement.config import CHROMEDRIVER

firefox = webdriver.Firefox(executable_path=CHROMEDRIVER)
firefox.implicitly_wait(5)
firefox.get("https://yandex.ru")

home_tabs = firefox.find_element(value="text")

# Получаем значение свойства innerHTML
html = home_tabs.get_property("innerHTML")
print(html)

# Получаем значение свойства data-bem
attr = home_tabs.get_attribute("data-bem")
print(attr)

# Получаем значение CSS войства margin-bottom
css = home_tabs.value_of_css_property("margin-bottom")
print(css)

firefox.close()