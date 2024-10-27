import pytest
from Tests.test_base import BaseTest
from Pages.HomePage import HomePage

class Test_Home(BaseTest):

    def test_FantasticFurnitureBrand_visibillity(self):
        self.homescreen=HomePage(self.driver)
        assert self.homescreen.is_FantasticFurnitureBrand_visible()

    def test_urlGetTitle(self):
        self.homescreen=HomePage(self.driver)
        title1=self.homescreen.get_homepage_title()
        assert title1=="Fantastic Furniture | Best Value Furniture, Mattresses & Decor | Shop Online"
        
        


    

