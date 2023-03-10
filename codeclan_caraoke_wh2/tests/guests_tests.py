import unittest
from src.guests import Guests

class TestGuests(unittest.TestCase):
    def setUp(self):
        self.guest_1 = ("Lewis")
        self.guest_2 = ("Claire")
        self.guest_3 = ("Keith")
        self.guest_4 = ("Jimbob")
        self.guest_5 = ("Divina")
        self.guest_6 = ("Lindsay")


        # Create rooms, songs and guests

    def test_guest_name(self):
        self.assertEqual("Lewis", self.guest_1)
        
