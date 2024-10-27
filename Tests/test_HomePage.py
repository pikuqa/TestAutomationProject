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

    def test_url(self):
        self.homescreen=HomePage(self.driver)
        current_url=self.homescreen.geturl()
        assert current_url=="https://www.fantasticfurniture.com.au/"
        
        


    

