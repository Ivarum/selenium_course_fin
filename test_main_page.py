from .pages.main_page import MainPage
import time


def test_guest_can_go_to_login_page(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()  # открываем страницу
    page.should_be_login_link()          # выполняем метод страницы — переходим на страницу логина