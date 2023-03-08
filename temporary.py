# from selenium.webdriver.firefox.options import Options as FirefoxOptions
# from selenium import webdriver
# options = FirefoxOptions()
# options.add_argument("--headless")
# options.add_argument('--no-sandbox')   

# # executable_path=DriverManager().install()
# driver = webdriver.Firefox(options=options)
# driver.get("https://pythonbasics.org")
# driver.close()

from selenium import webdriver

try:
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.add_argument("--headless")
    fireFoxOptions.add_argument('--no-sandbox')   
    brower = webdriver.Firefox(firefox_options=fireFoxOptions)

    brower.get('https://pythonbasics.org')
    print(brower.page_source)
finally:
    try:
        brower.close()
    except:
        pass