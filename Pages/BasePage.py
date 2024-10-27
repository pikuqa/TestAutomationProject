from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver=driver

    def do_click(self, locator):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator)).click()

    def do_sendKeys(self, locator, text):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_element_text(self, locator):
        elem=WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator))
        return elem.text
        
    def is_element_present(self, locator):
        try:
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
            
    def is_enabled(self, locator):
        elem1=WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator))
        return bool(elem1)
        
    def get_title(self):
        return self.driver.title    