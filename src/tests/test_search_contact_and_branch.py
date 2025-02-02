import ast

from src.helper.env_utils import get_env_variable
from src.pages.selenium_base_page import seleniumBasePage
from src.pages.login_page import LoginPage
from src.pages.home_page import HomePage
from src.pages.contacs_book_page import ContactsBookPage

class TestSearchContactAndBranch():
    base = seleniumBasePage()
    driver = base.selenium_start()
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    contacts_book_page = ContactsBookPage(driver)

    base_url = get_env_variable("BASE_URL", "https://example.com")
    driver.get(base_url)


    phone_number = get_env_variable("PHONE_NUMBER", "")
    login_page.login_by_phone(phone_number)
    login_page.login_btn()
    password = ast.literal_eval(get_env_variable("PASSWORD", ""))
    login_page.login_by_password(password)
    home_page.login_to_contacts_book()
    contacts_book_page.contact_search()
    contacts_book_page.branch_search()
    contacts_book_page.logout()



    print("All tests passed")
    base.selenium_end(driver)
