from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class AmazonHomePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.search_box = (By.ID, "twotabsearchtextbox")
        self.search_button = (By.ID, "nav-search-submit-button")

    def enter_search_keyword(self, keyword):
        self.driver.find_element(*self.search_box).send_keys(keyword)

    def click_search_button(self):
        self.driver.find_element(*self.search_button).click()