import unittest
from src.rooms import Rooms

class TestRooms(unittest.TestCase):
    def setUp(self):
        self.room_1 = Rooms("Mellow Vibes", 4)
        self.room_2 = Rooms("Power Balladsladslads", 6)
        self.room_3 = Rooms("Broken Air Conditioning", 8)

    def test_room_name(self):
        self.assertEqual("Power Balladsladslads", self.room_2.name)

    def test_room_capacity(self):
        self.assertEqual(8, self.room_3.capacity)