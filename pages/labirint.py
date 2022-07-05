import os
from pages.base_page import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements



class MainPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv(url)

        super().__init__(web_driver, url)

    #Main search field
    search = WebElement(id='search-field')

    #Search button
    search_run_button = WebElement(xpath='//*[@id="searchform"]/div[1]/button[1]')

    #Titles of the products in search results
    products_titles = ManyWebElements(xpath='//*[@id="rubric-tab"]/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]')
    delivery = WebElement(xpath='//*[@id="minwidth"]/div[6]/div[1]/div[2]/div[1]/ul[1]/li[1]/a[1]')
    certificates = WebElement(xpath='//*[@id="minwidth"]/div[6]/div[1]/div[2]/div[1]/ul[1]/li[2]/a[1]')
    rating = WebElement(xpath='//*[@id="minwidth"]/div[6]/div/div[2]/div/ul/li[3]/a')

    bonus_programs = WebElement(id='jslikeurl213')
    bonus_programs_text = WebElement(id='//*[@id="tdcard213"]')
    payment_method = WebElement(id='jslikeurl81')
    payment_method_text = WebElement(id='CardHelp81')



    shopping_cart_button = WebElement(id='buy660068')
    checkout = ManyWebElements(xpaht='//*[@id="basket-step1-default"]/div[2]/div[2]/div/div')

