# Sencha WebTestIt Page Object File

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageobjects.checkout_po import CheckoutPo


# Additional data: {"img":"screenshots/7c3f4e67-7fc6-4a37-ddeb-078a7513eb14.png"}
class CartPo:
    # Additional data: {"img":"screenshots/df6602e4-0a91-165e-d8b6-29fd07c116f7.png"}
    _proceed_to_checkout = (By.CSS_SELECTOR, ".checkout-button")
    """
    NOTE: Use Sencha to generate element code
    """
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)
        return self

    def get_title(self):
        return self.driver.title

    """
    NOTE: Drag elements from the Elements panel into the code editor to
    generate methods. Drag elements into existing methods to add steps.
    """
    def click_proceed_to_checkout(self):
        self.wait.until(
            EC.visibility_of_element_located(
                self._proceed_to_checkout)).click()

        return CheckoutPo(self.driver)
