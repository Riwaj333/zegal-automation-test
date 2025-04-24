import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

class SearchResultsPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.first_product_title = (By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[4]/div/div/div/div/span/div/div/div/div[2]/div/div/div[1]/a/h2/span')
        self.first_product_link = (By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[4]/div/div/div/div/span/div/div/div/div[1]/div/div[2]/div/span/a/div/img')

    def select_first_product(self):
        title_element = self.driver.find_element(*self.first_product_title)
        selected_product_title = title_element.text
        current_window = self.driver.current_window_handle
        self.driver.find_element(*self.first_product_link).click()

        return selected_product_title
