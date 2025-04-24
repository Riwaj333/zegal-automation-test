import unittest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()
        self.base_url = "https://www.amazon.in"

    def tearDown(self):
        self.driver.quit()