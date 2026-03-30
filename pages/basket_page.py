from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def is_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_BTN), "Product is in basket"
    
    def is_empty_basket_message_presented(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MSSG), "Product message is not on page"