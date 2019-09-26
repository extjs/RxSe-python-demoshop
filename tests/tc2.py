# Ranorex Webtestit Test File

from utils.base_test import BaseTest
from pageobjects.items_overview_po import ItemsOverviewPo


class Tc2(BaseTest):
    def test_fast_checkout(self):
        driver = self.get_driver()

        # Open the page
        overview = ItemsOverviewPo(driver).open(
            "https://demoshop.webtestit.com/")

        # Add items to the cart
        overview.add_item1_to_cart()
        overview.add_item2_to_cart()
        overview.add_item3_to_cart()

        # View cart
        cart = overview.click_on_cart()

        # Perform checkout
        checkout = cart.click_proceed_to_checkout()

        # Fill out the form
        checkout.set_first_name("Chuck")
        checkout.set_last_name("Norris")
        checkout.set_email("chuck.norris@test.com")

        # Place the order
        confirmation = checkout.place_order()

        # Assert that the ordered amount is correct
        self.assertEqual(confirmation.get_total_amount(), "€3,700.00")
