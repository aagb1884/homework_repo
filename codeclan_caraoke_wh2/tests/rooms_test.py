import unittest
from src.rooms import *
from src.songs import Songs
from src.guests import Guests

class TestRooms(unittest.TestCase):
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

    def test_room_name(self):
        self.assertEqual("Mellow Vibes", self.room_1.name)

    def test_room_capacity(self):
        self.assertEqual(4, self.room_1.capacity)

    def test_add_guest_to_room(self):
        self.assertEqual(0, len(self.room_2.guestlist))
        self.room_2.add_guest_to_room(self.guest_2)
        self.assertEqual(1, len(self.room_2.guestlist))

    
    def test_remove_guest_from_room(self):
        self.room_3.add_guest_to_room(self.guest_12)
        self.assertEqual(1, len(self.room_3.guestlist))
        self.room_3.remove_guest_from_room(self.guest_12)
        self.assertEqual(0, len(self.room_3.guestlist))