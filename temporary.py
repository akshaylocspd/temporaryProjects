
from webdriver_manager.firefox import  DriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
options = FirefoxOptions()
options.add_argument("--headless")

executable_path=DriverManager().install()
driver = webdriver.Firefox(options=options,executable_path=executable_path)
driver.get("https://pythonbasics.org")
driver.close()
