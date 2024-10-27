import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Config.config import Testdata



@pytest.fixture(params=["chrome"], scope="class")
def init_driver(request):
    s3=Service(Testdata.CHROME_executable_path)
    if request.param=="chrome":
        driver=webdriver.Chrome(service=s3)
    request.cls.driver=driver
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield
    driver.close()  