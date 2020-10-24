import unittest

from classes.song import *
from classes.room import *

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Believe", "Cher", "Pop", 159)

    def test_song_has_title(self):
        self.assertEqual("Believe", self.song.title)

    def test_song_has_artist(self):
        self.assertEqual("Cher", self.song.artist)

    def test_song_has_duration(self):
        self.assertEqual(159, self.song.duration)

    def test_add_song_works(self):
        song = Song("Wonderwall", "Oasis", "Rock", 220)
        self.song.add_song(song)
        self.assertEqual(1, len(self.song.playlist))

    def test_find_song__does_find_song(self):
        self.song.add_song(self.song)
        self.assertEqual(True, self.song.find_song("Believe"))

    def test_find_song__doesnt_find_song(self):
        self.song.add_song(self.song)
        self.assertEqual(False, self.song.find_song("Wonderwall"))

    def test_remove_song__does_find_song(self):
        self.song.add_song(self.song)
        self.song.remove_song("Believe")
        self.assertEqual(0, len(self.song.playlist))

    def test_remove_song__doesnt_find_song(self):
        self.song.add_song(self.song)
        self.song.remove_song("Wonderwall")
        self.assertEqual(1, len(self.song.playlist))

    