from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators():
    LOG_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASS_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    PASS_CONF_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    
    REG_BTN = (By.CSS_SELECTOR, "[name='registration_submit']")
class ProductPageLocators():
    ADD_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    
    SUCCES_ADD_MSG = (By.CSS_SELECTOR, ".alert-success:first-of-type .alertinner strong")
    NAME = (By.CSS_SELECTOR, ".product_main h1")
    
    BASKET_VAL = (By.CSS_SELECTOR, ".alertinner p strong")
    COST = (By.CSS_SELECTOR, ".product_main .price_color")
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a")
    BASKET_BTN = (By.CSS_SELECTOR, ".btn-primary")
    BASKET_EMPTY_MSSG = (By.CSS_SELECTOR, "#content_inner > p")
class ProfilePageLocators():
    DELETE_BTN = (By.CSS_SELECTOR, "#delete_profile")
    DEL_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_password")
    DEL_ACCEPT_BTN = (By.CSS_SELECTOR, ".btn-danger")