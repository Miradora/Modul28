#  python -m pytest -v --driver Chrome --driver-path C:/Users/1/PycharmProjects/Module_28/chromedriver.exe
import time
from pages.labirint import MainPage
from pages.base_page import WebPage

url = "https://www.labirint.ru/search/?discount=1&available=1&order=actd&way=back&paperbooks=1&ebooks=1&otherbooks=1"

def test_check_main_search(web_browser):
    """Make sure main search works fine."""
    page = MainPage(web_browser, url)
    page.search = 'Александр Беляев'
    page.search_run_button.click()
    assert page.products_titles.count() > 0

def test_menu(web_browser):

    page = MainPage(web_browser, url)
    page.delivery.is_presented()
    page.delivery.is_visible()
    page.delivery.wait_to_be_clickable()
    page.delivery.click()
    page.wait_page_loaded()
    page.go_back()

    page = MainPage(web_browser, url)
    page.certificates.is_presented()
    page.certificates.click()
    page.wait_page_loaded()
    page.go_back()

    page = MainPage(web_browser, url)
    page.rating.is_presented()
    page.rating.click()
    page.wait_page_loaded()
    page.go_back()


def test_adding_to_cart(web_browser):
    page = MainPage(web_browser, url)
    page.shopping_cart_button.scroll_to_element()
    page.shopping_cart_button.click()
    page.get('https://www.labirint.ru/cart/')
    time.sleep(2)


    assert page.checkout.count() > 0







