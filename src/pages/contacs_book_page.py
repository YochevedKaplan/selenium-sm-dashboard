import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ContactsBookPage():
    def __init__(self, driver):
        self.driver = driver

    def wait_for_requests_to_finish(self):
        start_time = time.time()
        while time.time() - start_time < 10:
            requests_active = self.driver.execute_script("""
                return window.performance.getEntriesByType('resource')
                       .filter(e => e.initiatorType === 'xmlhttprequest' || e.initiatorType === 'fetch')
                       .some(e => !e.responseEnd);
            """)
            if not requests_active:
                return
            time.sleep(0.5)


    def contact_search(self):
        self.wait_for_requests_to_finish()
        contact = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "shaliach-search-autocomplete-input")))
        contact.click()

        print("contact-search-complete")

        contact.send_keys("הרב מנחם מנדל ארבוב - אילת - המרכזי")
        contact = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "shaliach-search-autocomplete-input-option-0")))
        contact.click()

        print("contact specific Search Complete")

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'בית חב״ד אילת - המרכזי')]")))

        assert "בית חב״ד אילת - המרכזי" in self.driver.page_source, "Expected text 'בית חב״ד אילת - המרכזי' not found on the page"
        assert "Layer_2-2" in self.driver.page_source, "Email button not found on the page"


    def branch_search(self):
        self.driver.refresh()
        self.wait_for_requests_to_finish()
        branch = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.ID, "branch-search-autocomplete-input")))
        branch.click()

        print("Branch Search Complete")

        branch.send_keys("אחיעזר")
        branch = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.ID, "branch-search-autocomplete-input-option-0")))
        branch.click()

        print("Branch specific Search Complete")

        WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'בית חב״ד אחיעזר')]")))

        assert "בית חב״ד אחיעזר" in self.driver.page_source, "Expected text 'בית חב״ד אחיעזר' not found on the page"

    def logout(self):
        logout = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid ="profile-button"]')))
        logout.click()
        logout = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid ="logout-button"]')))
        logout.click()

        print("Logout Complete")

