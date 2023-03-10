import unittest
from src.guests import Guests

class TestGuests(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guests("Lewis")
        self.guest_2 = Guests("Claire")
        self.guest_3 = Guests("Keith")
        self.guest_4 = Guests("Jimbob")
        self.guest_5 = Guests("Divina")
        self.guest_6 = Guests("Lindsay")
        self.guest_7 = Guests("Hilda")
        self.guest_8 = Guests("Bluey's Dad")
        self.guest_9 = Guests("Id Monster")
        self.guest_10 = Guests("Omega")
        self.guest_11 = Guests("Rassilon")
        self.guest_12 = Guests("Tecteun")

    def test_guest_name(self):
        self.assertEqual("Lewis", self.guest_1)