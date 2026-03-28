from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators():
    LOG_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
class ProductPageLocators():
    ADD_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    
    SUCCES_ADD_MSG = (By.CSS_SELECTOR, ".alert-success:first-of-type .alertinner strong")
    NAME = (By.CSS_SELECTOR, ".product_main h1")
    
    BASKET_VAL = (By.CSS_SELECTOR, ".alertinner p strong")
    COST = (By.CSS_SELECTOR, ".product_main .price_color")
    