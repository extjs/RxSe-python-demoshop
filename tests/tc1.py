# Ranorex Webtestit Test File

from utils.base_test import BaseTest
from pageobjects.items_overview_po import ItemsOverviewPo
from pageobjects.header_po import HeaderPo


class Tc1(BaseTest):
    def test_check_for_total_amount_using_3_items(self):
        driver = self.get_driver()

        # Open the page
        overview = ItemsOverviewPo(driver).open(
            "https://demoshop.webtestit.com/")

        # Add item to the cart
        overview.add_item1_to_cart()
        overview.add_item2_to_cart()
        overview.add_item3_to_cart()

        # Perform checkout
        header = HeaderPo(driver)
        checkout = header.go_to_checkout()

        # Fill out the form
        checkout.set_first_name("Chuck")
        checkout.set_last_name("Norris")
        checkout.set_email("chuck.norris@test.com")

        # Place the order
        confirmation = checkout.place_order()

        # Assert that the ordered amount is correct
        self.assertEqual(confirmation.get_total_amount(), "€3,700.00")

    def test_check_for_total_amount_using_1_item(self):
        driver = self.get_driver()

        overview = ItemsOverviewPo(driver).open(
            "https://demoshop.webtestit.com/")

        # Add item to the cart
        overview.add_item1_to_cart()

        # Perform checkout
        header = HeaderPo(driver)
        checkout = header.go_to_checkout()

        # Fill out the form
        checkout.set_first_name("Chuck")
        checkout.set_last_name("Norris")
        checkout.set_email("chuck.norris@test.com")

        # Place the order
        confirmation = checkout.place_order()

        # Assert that the ordered amount is correct
        self.assertEqual(confirmation.get_total_amount(), "€1,500.00")
