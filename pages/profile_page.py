from .base_page import BasePage
from .locators import ProfilePageLocators

class ProfilePage(BasePage):
    def deleting_account(self, password):
        delete_btn = self.browser.find_element(*ProfilePageLocators.DELETE_BTN)
        delete_field = self.browser.find_element(*ProfilePageLocators.DEL_PASSWORD_FIELD)
        del_accept_btn = self.browser.find_element(*ProfilePageLocators.DEL_ACCEPT_BTN)
        delete_btn.click
        delete_field.send_keys(password)
        del_accept_btn.click
        