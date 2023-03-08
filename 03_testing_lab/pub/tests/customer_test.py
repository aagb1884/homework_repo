import unittest

from src.customer import Customer
from src.drink import Drink
from src.pub import Pub

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Jammo", 10.00, 21, 0)
        self.drink = Drink("Beer", 3.00, 20)
        self.pub = Pub("The Crass Badger", 100.00)

    def test_customer_has_name(self):
        self.assertEqual("Jammo", self.customer.name)

    def test_customer_has_money(self):
        self.assertEqual(10.00, self.customer.wallet)

    def test_buy_drink(self):
        self.customer.buy_drink(self.drink)
        self.assertEqual(7.00, self.customer.wallet)
        self.assertEqual(20, self.customer.drunkenness)