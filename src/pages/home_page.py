from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class HomePage():
    def __init__(self, driver):
        self.driver = driver

    def login_to_contacts_book(self):
        contacts_book_btn = WebDriverWait (self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-testid ="nav-item-8"]')))
        contacts_book_btn.click()

        print("Welcome to Contacts Book")


