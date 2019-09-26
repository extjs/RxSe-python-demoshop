# Ranorex Webtestit Page Object File

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageobjects.cart_po import CartPo
from pageobjects.header_po import HeaderPo


# Additional data: {"img":"screenshots/4938e677-5b33-d27e-6529-f19313650d7f.png"}
class ItemsOverviewPo:
    # Additional data: {"img":"screenshots/61da7e72-86f1-98ae-e897-b7c68f46cca8.png"}
    _item1_add_to_cart_button = (By.CSS_SELECTOR, "[data-product_id='8']")
    # Additional data: {"img":"screenshots/a8ee897e-1712-db39-a9f8-337a702d876b.png"}
    _item2_add_to_cart_button = (By.CSS_SELECTOR, "[data-product_id='9']")
    # Additional data: {"img":"screenshots/556b743d-74d9-d45c-e58d-86b85799983b.png"}
    _item3_add_to_cart_button = (By.CSS_SELECTOR, "[data-product_id='10']")
    # Additional data: {"img":"screenshots/c408d682-a219-97f8-fdd4-f692461bd6aa.png"}
    _item_3_view_cart_button = (By.CSS_SELECTOR, "[title='View cart']")
    _blocker = (By.CSS_SELECTOR, ".blockOverla")
    """
    NOTE: Use Ranorex Selocity or the Elements Panel to generate element code
    """
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        driver.implicitly_wait(2)

    def open(self, url):
        self.driver.get(url)
        return self

    def get_title(self):
        return self.driver.title

    """
    NOTE: Drag elements from the Elements panel into the code editor to
    generate methods. Drag elements into existing methods to add steps.
    """
    def add_item1_to_cart(self):
        self.wait.until(
            EC.visibility_of_element_located(
                self._item1_add_to_cart_button)).click()
        self.wait.until(EC.invisibility_of_element_located(self._blocker))

        return self

    def add_item2_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self._item2_add_to_cart_button)).click()
        self.wait.until(EC.invisibility_of_element_located(self._blocker))

        return self

    def add_item3_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self._item3_add_to_cart_button)).click()
        self.wait.until(EC.invisibility_of_element_located(self._blocker))

        return HeaderPo(self.driver)

    def click_on_cart(self):
        self.wait.until(
            EC.visibility_of_element_located(
                self._item_3_view_cart_button)).click()
        self.wait.until(EC.invisibility_of_element_located(self._blocker))

        return CartPo(self.driver)
