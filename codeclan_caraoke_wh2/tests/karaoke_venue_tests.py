import unittest
from src.karaoke_venue import *
from src.rooms import Rooms
from src.guests import Guests
from src.songs import Songs

class TestVenue(unittest.TestCase):
    def setUp(self):
        
        self.room_1 = Rooms("Mellow Vibes", 4)
        self.room_2 = Rooms("Power Balladsladslads", 6)
        self.room_3 = Rooms("Broken Air Conditioning", 8)
        self.room_list = [self.room_1, self.room_2, self.room_3]

        self.song_1 = Songs("Undone (The Sweater Song)", "Weezer")
        self.song_2 = Songs("Song 2", "Blur")
        self.song_3 = Songs("Angels", "Robbie Williams")
        self.song_4 = Songs("You Oughta Know", "Alanis Morissette")
        self.song_5 = Songs("River", "Joni Mitchell")
        self.song_6 = Songs("Toungescraper I & II", "Desalvo")
        self.song_7 = Songs("Basscadet", "Autechre")
     
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

        self.venue = Venue("Sing Hole",
                           [self.room_1, self.room_2, self.room_3])

    def test_venue_name(self):
        self.assertEqual
        ("Sing Hole", self.venue.name)
        
    def test_room_name(self):
        self.assertEqual("Mellow Vibes", self.room_1.name)
    def test_room_capacity(self):
        self.assertEqual(4, self.room_1.capacity)   

    def test_song_name(self):
        self.assertEqual("River", self.song_5.name)    
    def test_song_artist(self): 
        self.assertEqual("Desalvo", self.song_6.artist)

    def test_guest_name(self):
        self.assertEqual("Jimbob", self.guest_4.name)

    def test_check_guest_into_venue(self):
        self.assertEqual(0, len(self.venue.guests))
        self.venue.check_guest_into_venue(self.guest_1)
        self.assertEqual(1, len(self.venue.guests))
   
    def test_remove_guest_from_venue(self):
        self.venue.check_guest_into_venue(self.guest_1)
        self.assertEqual(1, len(self.venue.guests))
        self.venue.remove_guest_from_venue(self.guest_1)
        self.assertEqual(0, len(self.venue.guests))

        # add rooms to list, references in tests above for that.
        # add guestlist to rooms.py so guests can be added/counted
        # refer back to past labs for examples of ACT
        # to check guest into room need room and guest
        # once guest added to room should be part of room so
        # just refer to room
        