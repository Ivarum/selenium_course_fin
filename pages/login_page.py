from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Not login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOG_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Register form is not presented"
    
    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        password_field = self.browser.find_element(*LoginPageLocators.PASS_FIELD)
        password_confirm_field = self.browser.find_element(*LoginPageLocators.PASS_CONF_FIELD)
        email_field.send_keys(email)
        password_field.send_keys(password)
        password_confirm_field.send_keys(password)
        registration_btn = self.browser.find_element(*LoginPageLocators.REG_BTN)
        registration_btn.click