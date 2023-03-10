import unittest
from src.songs import Songs

class TestSongs(unittest.TestCase):
    def setUp(self):
        self.song_1 = Songs("Undone (The Sweater Song)", "Weezer")
        self.song_2 = Songs("Song 2", "Blur")
        self.song_3 = Songs("Angels", "Robbie Williams")
        self.song_4 = Songs("You Oughta Know", "Alanis Morissette")
        self.song_5 = Songs("River", "Joni Mitchell")
        self.song_6 = Songs("Toungescraper I & II", "Desalvo")
        self.song_7 = Songs("Basscadet", "Autechre")


    def test_song_name(self):
        self.assertEqual("Song 2", self.song_2.name)


    def test_song_artist(self):
        self.assertEqual("Joni Mitchell", self.song_5.artist)