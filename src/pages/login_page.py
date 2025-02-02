from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class LoginPage():
    def __init__(self, driver):
        self.driver = driver


    def login_by_phone(self, phone_number):
        user = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-testid="phone-input"]')))
        user.click()
        user.send_keys(phone_number)

        print("Login by phone successfully")


    def login_btn(self):

        login_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="login-button"]')))
        login_btn.click()

        print("Login successfully")


    def login_by_password(self, otp_input):


        for i in range (len(otp_input)):
            otp_digit = otp_input[i]
            otp_input_field = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f'[data-testid="pin-code-input-{i}"]')))
            otp_input_field.send_keys(otp_digit)

        print("otp input successfully")



