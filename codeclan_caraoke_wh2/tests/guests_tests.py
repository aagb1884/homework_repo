import unittest
from src.guests import Guests

class TestGuests(unittest.TestCase):
    def setUp(self):

     def test_guest_name(self):
         self.guest_1 = Guests("Lewis")
         self.assertEqual("Lewis", self.guest_1)