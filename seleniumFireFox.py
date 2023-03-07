from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.options import Options
try:
    options = Options()
    # this parameter tells Chrome that
    # it should be run without UI (Headless)
    # options.headless = True
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    
    executable_path=ChromeDriverManager(version="89.0.4389.114",chrome_type=ChromeType.CHROMIUM).install()
    brower = webdriver.Chrome(options=options)
    brower.get('https://pythonbasics.org')
    print(brower.page_source)
finally:
    try:
        brower.close()
    except:
        pass