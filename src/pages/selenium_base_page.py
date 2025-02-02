from selenium.webdriver.chrome.options import Options
from selenium import webdriver


class seleniumBasePage():

    def selenium_start(self):
        print("start test")
        options = Options()

        options.add_argument('--no-sandbox')
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        options.add_argument("--start-fullscreen")
        options.add_argument('--disable-gpu')

        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        return driver

    def selenium_end(self,driver):
        print ("selenium end")
        driver.close()