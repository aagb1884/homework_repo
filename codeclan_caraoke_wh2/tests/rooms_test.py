import unittest
from src.rooms import Rooms

class TestRooms(unittest.TestCase):
    def setUp(self):
        self.room_1 = Rooms("Mellow Vibes", 8)
        self.room_2 = Rooms("Power Balladsladslads", 10)
        self.room_3 = Rooms("Broken Air Conditioning", 12)


        # Create rooms, songs and guests

    def test_room_name(self):
        self.assertEqual("Power Balladsladslads", self.room_2.name)

    def test_room_capacity(self):
        self.assertEqual(12, self.room_3.capacity)