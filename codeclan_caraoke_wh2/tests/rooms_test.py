import unittest
from src.rooms import Rooms

class TestRooms(unittest.TestCase):
    def setUp(self):
        self.room_1 = Rooms("Mellow Vibes", 4)

    def test_room_name(self):
        self.assertEqual("Mellow Vibes", self.room_1.name)

    def test_room_capacity(self):
        self.assertEqual(4, self.room_1.capacity)