from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
options = FirefoxOptions()
options.add_argument("--headless")
options.add_argument('--no-sandbox')   

# executable_path=DriverManager().install()
driver = webdriver.Firefox(options=options)
driver.get("https://pythonbasics.org")
driver.close()