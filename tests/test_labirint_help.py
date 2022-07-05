#  python -m pytest -v --driver Chrome --driver-path C:/Users/1/PycharmProjects/Module_28/chromedriver.exe
from pages.base_page import WebPage

from pages.labirint import MainPage
url = 'https://www.labirint.ru/help/'

def test_site_help(web_browser):
    page = MainPage(web_browser, url)

    page.bonus_programs.find()
    page.bonus_programs.click()
    page.bonus_programs_text.is_presented()
    page.bonus_programs.click()

    page.payment_method.find()
    page.payment_method.click()
    page.payment_method_text.is_presented()
    page.payment_method.click()









