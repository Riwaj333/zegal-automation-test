import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObject.amazon_home import AmazonHomePage
from pageObject.SearchResultPage import SearchResultsPage
from pageObject.ProductDetailPage import ProductDetailsPage
from testCases.setup import BaseTest

class TestAddToCart(BaseTest):
    def test_search_product_and_add_to_cart(self):

        self.driver.get(self.base_url)
        amazon_home = AmazonHomePage(self.driver)


        search_keyword = "Gaming Mouse"
        amazon_home.enter_search_keyword(search_keyword)
        amazon_home.click_search_button()
        current_window = self.driver.current_window_handle

        search_results_page = SearchResultsPage(self.driver)


        selected_product_title = search_results_page.select_first_product()
        WebDriverWait(self.driver, 10).until(
            lambda d: len(d.window_handles) > 1  # Wait until there is more than one window/tab
        )
        new_window = [window for window in self.driver.window_handles if window != current_window][0]
        self.driver.switch_to.window(new_window)


        product_details_page = ProductDetailsPage(self.driver)


        product_details_page.click_add_to_cart()


        cart_product_title_element = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[3]/div[5]/div/div[2]/div[1]/div/form/div[2]/div[3]/div[4]/div/div[2]/ul/li/span/a/span[1]/h4/span/span[2]')
        cart_product_title = cart_product_title_element.text


        assert selected_product_title[:30].lower() in cart_product_title.lower(), \
            f"Expected part of '{selected_product_title}' to be in '{cart_product_title}'"


if __name__ == '__main__':
    unittest.main()