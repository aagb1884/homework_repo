import unittest
from src.karaoke_venue import Venue
from src.rooms import Rooms
from src.guests import Guests
from src.songs import Songs

class TestVenue(unittest.TestCase):
    def setUp(self):
        self.name = Venue("Come and have a go if you think you're bard enough")
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
        self.song_list = [self.song_1, self.song_2,
                          self.song_3, self.song_4,
                          self.song_5, self.song_6,
                          self.song_7]
        
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
        self.guest_list = [self.guest_1, self.guest_2,
                           self.guest_3, self.guest_4,
                           self.guest_5, self.guest_6,
                           self.guest_7, self.guest_8,
                           self.guest_9, self.guest_10,
                           self.guest_11, self.guest_12]
        


    def test_venue_name(self):
        self.assertEqual
        ("Come and have a go if you think you're bard enough", 
         self.name)
        
    def test_room_name(self):
        self.assertEqual("Mellow Vibes", self.room_list[0].name)
    def test_room_capacity(self):
        self.assertEqual(4, self.room_list[0].capacity)   

    def test_song_name(self):
        self.assertEqual("River", self.song_list[4].name)    
    def test_song_artist(self): 
        self.assertEqual("Desalvo", self.song_list[5].artist)

    def test_guest_name(self):
        self.assertEqual("Jimbob", self.guest_list[3].name)