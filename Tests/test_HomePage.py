import pytest
from Tests.test_base import BaseTest
from Pages.HomePage import HomePage
import time

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
    
    def test_is_searchbox_present(self):
        self.homescreen=HomePage(self.driver)
        assert self.homescreen.is_serachbox_present()

    def test_successful_cartmessage(self):
        self.homescreen=HomePage(self.driver)
        self.homescreen.add_to_cart_jordan_single_bed()
        Actual_message=self.homescreen.cart_message()
        expected_message="Item was added to your cart"
        assert Actual_message==expected_message, "this test case is not passed 3105"



        
        


    

