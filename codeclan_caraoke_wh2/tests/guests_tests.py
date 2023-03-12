import unittest
from src.guests import Guests

class TestGuests(unittest.TestCase):
    def setUp(self):

     def test_guest_name(self):
         self.guest_1 = Guests("Lewis", 10)
         self.assertEqual("Lewis", self.guest_1.name)

    def test_guest_wallet(self):
         self.guest_1 = Guests("Lewis", 10)
         self.assertEqual(10, self.guest_1.wallet)