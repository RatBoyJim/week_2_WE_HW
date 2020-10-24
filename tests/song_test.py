import unittest

from classes.song import *

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Believe", "Cher", "Pop", 159)

    def test_song_has_title(self):
        self.assertEqual("Believe", self.song.title)

    def test_song_has_artist(self):
        self.assertEqual("Cher", self.song.artist)

    def test_song_has_duration(self):
        self.assertEqual(159, self.song.duration)

    