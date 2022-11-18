from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome, Firefox, Remote
from selenium.webdriver.chrome.options import Options

driver = Chrome(executable_path=ChromeDriverManager().install())

