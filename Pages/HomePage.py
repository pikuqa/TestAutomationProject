from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import Testdata
from selenium import webdriver
import time

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Testdata.BaseURL)
        self.FantasticFurnitureBrand=(By.XPATH, '(//div[contains(text(),"Best Value Furniture and Bedding")])[1]')
        self.search_box=(By.XPATH, '(//img[@class="ng-tns-c1215374474-0"])[1]')
        self.Bedroom_Matresses=(By.XPATH, '//nav/a[text()=" Bedroom & Mattresses "]')
        self.single_beds=(By.XPATH, '(//nav/a[text()=" Bedroom & Mattresses "]//following::li/a[text()="Single Beds"])[1]')
        self.add_to_cart_singlebeds=(By.XPATH, '//div/div[text()="Oasis Single Bed"]//preceding::button[@class="cartBtn ng-star-inserted"]')
        self.cart_message=(By.XPATH, '//span[@class="cart-success-header__text"]')
    
    def is_FantasticFurnitureBrand_visible(self):
        return self.is_enabled(self.FantasticFurnitureBrand)


    def get_homepage_title(self):
        return self.get_title()    
    
    def geturl(self):
        return self.driver.current_url
    
    def is_serachbox_present(self):
        return self.is_element_present(self.search_box)
    
    def add_to_cart_jordan_single_bed(self):
        self.mouse_hover_scroll(self.Bedroom_Matresses)
        self.do_click(self.single_beds)
        self.mouse_hover_scroll(self.add_to_cart_singlebeds)
        return self.do_click(self.add_to_cart_singlebeds)
    
    def method_cart_message(self):
        return self.get_element_text(self.cart_message)
        
     

    