from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import Testdata
from selenium import webdriver

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Testdata.BaseURL)
        self.FantasticFurnitureBrand=(By.XPATH, '(//div[contains(text(),"Best Value Furniture and Bedding")])[1]')

    
    
    def is_FantasticFurnitureBrand_visible(self):
        return self.is_enabled(self.FantasticFurnitureBrand)


    def get_homepage_title(self):
        return self.get_title()    

    