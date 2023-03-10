import unittest
from src.karaoke_venue import Venue
from src.rooms import Rooms
from src.guests import Guests
from src.songs import Songs

class TestVenue(unittest.TestCase):
    def setUp(self):
        self.name = Venue("Come and have a go if you think you're bard enough")
        
    def test_venue_name(self):
        self.assertEqual
        ("Come and have a go if you think you're bard enough", 
         self.name)
  