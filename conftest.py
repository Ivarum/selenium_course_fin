import pytest
import faker
from .pages.locators import BasePageLocators
from .pages.login_page import LoginPage
from .pages.profile_page import ProfilePage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption("--language", action="store", default='en',
                     help="Choose your language: ru, en, ec, fr",)

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("--language")
    options = Options()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language})
    options.add_argument(f"--lang={user_language}")

    options_firefox = OptionsFirefox()
    options_firefox.set_preference("intl.accept_languages", user_language)

    browser_name = request.config.getoption("browser_name")
    browser = None
    
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(options=options_firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
@pytest.fixture(scope="function", autouse=True)
def setup(browser):
    f = faker.Faker()
    password = "Qwerty123321"
    email = f.email()
    login_page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/ru/accounts/login/")
    login_page.open()
    login_page.register_new_user(email, password)
    login_page.is_element_present(*BasePageLocators.USER_ICON)
    yield
    profile_page = ProfilePage(browser, "http://selenium1py.pythonanywhere.com/ru/accounts/profile/")
    profile_page.open()
    profile_page.deleting_account(password)
    
    

