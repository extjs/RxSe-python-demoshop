# Ranorex Webtestit Page Object File

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Additional data: {"img":"screenshots/0494bfd5-f74e-934d-206d-0312f47a91a4.png"}
class ConfirmationPo:
    # Additional data: {"img":"screenshots/8c3b988e-a863-d385-7605-f9a60b6bdbc3.png"}
    _total_amount = (By.CSS_SELECTOR, "tfoot tr:nth-of-type(3) .woocommerce-Price-amount")
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
    def get_total_amount(self):
        total_amout_text = self.wait.until(
            EC.visibility_of_element_located(self._total_amount)).text

        return total_amout_text
