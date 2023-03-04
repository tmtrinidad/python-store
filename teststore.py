# ----------------------------------------------------------------------
# Name:      test store
# Author(s): taylor trinidad
# ----------------------------------------------------------------------
"""
Test cases for store.py

This program provides test cases against the restock, review, sell, lowest
price and average rating methods
"""

import unittest
import store


class TestRestock(unittest.TestCase):
    """
    Test case for Restock method
    """
    def setUp(self):
        """
        Creates a product for testing
        """
        self.item = store.Product("Wallet", 10)
        self.item.stock = 10

    def test_restock_success(self):
        """
        Test restock on an account with a positive value
        """
        self.assertIsNone(self.item.restock(10))  # should return None
        self.assertEqual(self.item.stock, 20)  # desired update
        self.assertEqual(self.item.description, "Wallet")
        self.assertEqual(self.item.list_price, 10)

    def test_restock_failure(self):
        """
        Test restock on an account with a negative value
        """
        self.assertIsNone(self.item.restock(-10))  # should return None
        self.assertEqual(self.item.stock, 0)  # desired update
        self.assertEqual(self.item.description, "Wallet")
        self.assertEqual(self.item.list_price, 10)


class TestReview(unittest.TestCase):
    """
    Test case for Review method
    """

    def setUp(self):
        """ Create a Product for testing. """
        self.item = store.Product("iPhone 14", 1000)

    def test_review_success(self):
        self.assertIsNone(self.item.review(5, "great display"))  # return value
        self.assertEqual(self.item.reviews[0], ("great display",
                                                5))  # desired update

    def test_review_negative(self):
        self.assertIsNone(self.item.review(-1, "bad battery life"))  # return
        # value
        self.assertGreaterEqual(int(self.item.reviews[0][1]), 0)  # desired
        # update

    def test_review_int_text(self):
        self.assertIsNone(self.item.review(4, 5))  # return value
        self.assertEqual(self.item.reviews, [])  # shouldn't allow reviews
        # with bad input for "text" argument


class TestSell(unittest.TestCase):
    """
    Test Case for the Sell method
    """
    def setUp(self):
        """
        Creates a product for testing
        """
        self.item = store.Product("Phone charger", 5)
        self.item.stock = 2

    def test_sell_success(self):
        """
        Tests selling a item with enough quantity to fulfill
        """
        self.assertIsNone(self.item.sell(1))  # should return None
        self.assertEqual(self.item.stock, 1)  # desired update
        self.assertEqual(self.item.description, "Phone charger")
        self.assertEqual(self.item.list_price, 5)

    def test_sell_success(self):
        """
        Tests selling a item with not enough quantity to fulfill
        """
        self.assertIsNone(self.item.sell(5))  # should return None
        self.assertEqual(self.item.stock, 0)  # desired update
        self.assertEqual(self.item.description, "Phone charger")
        self.assertEqual(self.item.list_price, 5)


class TestLowestPrice(unittest.TestCase):
    """
    Test case for lowest_price method
    """

    def setUp(self):
        """ Create a Product for testing. """
        self.item = store.Product("iPhone 14", 1000)

    def test_lowest_price(self):
        """ Test lowest price for normal case. """
        self.item.sales.append(1000)
        self.item.sales.append(800)
        self.assertEqual(self.item.lowest_price, 800)
        self.assertEqual(self.item.list_price, 1000)

    def test_lowest_price_no_sales(self):
        """ Test lowest price when no sales have been made """
        self.assertIsNone(self.item.lowest_price)


class TestAverageRating(unittest.TestCase):
    """
    Test case for Average Rating method
    """
    def setUp(self):
        """
        Creates a product for testing
        """
        self.item = store.Product("Phone charger", 5)

    def test_average_rating_empty(self):
        """
        Tests an item with no ratings
        """
        self.assertEqual(self.item.average_rating, "None")  # desired update
        self.assertEqual(self.item.description, "Phone charger")
        self.assertEqual(self.item.list_price, 5)

    def test_average_rating_success(self):
        """
        Tests an item with ratings
        """
        self.item.review(5, 'Works great.')
        self.item.review(3, 'Good but broke after a couple years')
        self.item.review(4, 'Good but expensive')

        self.assertEqual(self.item.average_rating, 4)  # desired update
        self.assertEqual(self.item.description, "Phone charger")
        self.assertEqual(self.item.list_price, 5)
