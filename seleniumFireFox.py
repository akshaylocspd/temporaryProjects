from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.service import Service
import os
from selenium.webdriver.chrome.options import Options
def getCurrentDirPath():
    return os.getcwd() 
try:
    print ('hanuman please help')
    options = Options()
    # this parameter tells Chrome that
    # it should be run without UI (Headless)
    # options.headless = True
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    # notsfasd
    # executable_path=ChromeDriverManager(chrome_type=ChromeType.CHROMIUM,path=getCurrentDirPath()).install()
    brower = webdriver.Chrome(options=options,executable_path="/chromedriver")
    brower.get('https://pythonbasics.org')
    print(brower.page_source)
finally:
    try:
        brower.close()
    except:
        pass