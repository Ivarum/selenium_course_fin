from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_backet(self):
        add_btn = self.browser.find_element(*ProductPageLocators.ADD_BTN)
        add_btn.click()
    def add_to_basket_name_check(self):
        assert self.browser.find_element(*ProductPageLocators.SUCCES_ADD_MSG).text == self.browser.find_element(*ProductPageLocators.NAME).text, "Not correct product name in message"
    def add_to_basket_cost_check(self): 
        assert self.browser.find_element(*ProductPageLocators.BASKET_VAL).text == self.browser.find_element(*ProductPageLocators.COST).text, "Not correct product cost in message"
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCES_ADD_MSG), "Success message is presented, but should not be"
    def disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCES_ADD_MSG), "Success message is not disappear"