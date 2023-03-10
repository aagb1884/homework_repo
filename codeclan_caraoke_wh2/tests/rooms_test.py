import unittest
from src.rooms import Rooms

class TestRooms(unittest.TestCase):
    def setUp(self):
        self.room_1("Mellow Vibes", 8)
        self.room_2("Power Balladsladslads", 10)
        self.room_3("Broken Air Conditioning", 12)


        # Create rooms, songs and guests