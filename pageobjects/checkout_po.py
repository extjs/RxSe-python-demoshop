# Sencha WebTestIt Page Object File

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageobjects.confirmation_po import ConfirmationPo


# Additional data: {"img":"screenshots/defcc5d6-ddd4-6830-875b-c5eecf6f9b9c.png"}
class CheckoutPo:
    # Additional data: {"img":"screenshots/772bb399-b2c7-3a9a-4fc7-89a10d9b8914.png"}
    _first_name = (By.CSS_SELECTOR, "[autocomplete='given-name']")
    # Additional data: {"img":"screenshots/ae222ab1-abf8-b307-e632-1a2128b72fff.png"}
    _last_name = (By.CSS_SELECTOR, "[autocomplete='family-name']")
    # Additional data: {"img":"screenshots/3b013064-1dc5-b3b9-e918-e08eb4c4fbef.png"}
    _email_address = (By.CSS_SELECTOR, "[autocomplete='email username']")
    # Additional data: {"img":"screenshots/4c056d4f-fe2d-424e-a177-e28c35427e90.png"}
    _woocommerce_checkout_place_order = (By.CSS_SELECTOR,
                                         "[value='Place order']")
    """
    NOTE: Use Sencha to generate element code
    """
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open(self, url):
        self.driver.get(url)
        return self

    def get_title(self):
        return self.driver.title

    """
    NOTE: Drag elements from the Elements panel into the code editor to
    generate methods. Drag elements into existing methods to add steps.
    """
    def set_first_name(self, text):
        self.wait.until(EC.visibility_of_element_located(
            self._first_name)).send_keys(text)

        return self

    def set_last_name(self, text):
        self.wait.until(EC.visibility_of_element_located(
            self._last_name)).send_keys(text)

        return self

    def set_email(self, text):
        self.wait.until(EC.visibility_of_element_located(
            self._email_address)).send_keys(text)

        return self

    def place_order(self):
        self.wait.until(
            EC.visibility_of_element_located(
                self._woocommerce_checkout_place_order)).click()

        return ConfirmationPo(self.driver)
