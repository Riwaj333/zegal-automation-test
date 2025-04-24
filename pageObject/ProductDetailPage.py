import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class ProductDetailsPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.add_to_cart_button = (By.ID, 'add-to-cart-button')
        # self.side_sheet_checkout_button = (By.ID, 'attach-sidesheet-checkout-button')
        self.view_cart_button = (By.XPATH, '/html/body/div[1]/div[1]/div/div[1]/div[2]/div/div[3]/div/div[1]/span/span/a')
        self.go_cart_button = (By.XPATH, '/html/body/div[1]/div[1]/div/div[1]/div[2]/div/div[3]/div/div[1]/span/span/a')

    def click_add_to_cart(self):
        try:
            # Try clicking primary Add to Cart button
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.ID, "add-to-cart-button"))
                ).click()
            except TimeoutException:
                # Try fallback ID
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.ID, "submit.add-to-cart"))
                ).click()

            # Wait for potential protection plan modal and dismiss it
            try:
                no_thanks_button = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.ID, "attachSiNoCoverage"))
                )
                no_thanks_button.click()
            except TimeoutException:
                pass  # No modal shown

            # Wait for cart confirmation UI (either side sheet or redirect buttons)
            # try:
            #     WebDriverWait(self.driver, 7).until(
            #         EC.element_to_be_clickable(self.side_sheet_checkout_button)
            #     ).click()
            # except TimeoutException:
            #     print("Side sheet not shown. Trying fallback cart view...")

                try:
                    WebDriverWait(self.driver, 7).until(
                        EC.element_to_be_clickable((By.ID, "nav-cart"))
                    ).click()
                except TimeoutException:
                    print("Fallback cart icon also not clickable.")

        except Exception as e:
            print(f"[ERROR] Failed to add product to cart: {e}")
            raise




