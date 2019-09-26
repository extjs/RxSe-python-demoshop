# Ranorex Webtestit Page Object File

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageobjects.checkout_po import CheckoutPo


class HeaderPo:
    # Additional data: {"img":"screenshots/c5d66ea0-c97e-37c3-2d04-74efa303f128.png"}
    _checkout = (
        By.CSS_SELECTOR,
        ".nav-menu [href='https\\:\\/\\/demoshop\\.webtestit\\.com\\/checkout\\/']"
    )
    """
    NOTE: Use Ranorex Selocity or the Elements Panel to generate element code
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
    def go_to_checkout(self):
        self.wait.until(EC.visibility_of_element_located(
            self._checkout)).click()

        return CheckoutPo(self.driver)
