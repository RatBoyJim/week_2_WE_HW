import unittest

from classes.room import *
from classes.guest import *
from classes.song import *
from classes.bar import *
from classes.drink import *
from classes.food import *

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Top o' the Pops", 2, 10)
        self.guest = Guest("Michael", 50.00, "Anderson", "Sometimes", 38)
        self.song = Song("Sometimes", "James", "Pop", 316)
        self.bar = Bar("The Tubthumper", 100.00)
        self.drink = Drink("Whisky Drink", 5.50, 1)
        self.food = Food("American Pie", 7.20, 3)

    def test_room_has_name(self):
        self.assertEqual("Top o' the Pops", self.room.name)

    def test_room_has_capacity(self):
        self.assertEqual(2, self.room.capacity)
    
    def test_room_has_price(self):
        self.assertEqual(10, self.room.price)

    def test_add_room_works(self):
        room = Room("Excellent Eighties", 25, 50)
        self.room.add_room(room)
        self.assertEqual(1, len(self.room.room_list))

    def test_add_guest_works(self):
        guest = Guest("Marie", 100, "Anderson", "I'll Be There For You", 38)
        self.room.add_guest(guest, self.bar)
        self.assertEqual(1, len(self.room.guest_list))

    def test_find_guest__does_find_guest(self):
        self.room.add_guest(self.guest, self.bar)
        self.assertEqual(True, self.room.find_guest("Michael"))

    def test_find_guest__doesnt_find_guest(self):
        self.room.add_guest(self.guest, self.bar)
        self.assertEqual(False, self.room.find_guest("Marie"))

    def test_remove_guest__does_find_guest(self):
        self.room.add_guest(self.guest, self.bar)
        self.room.remove_guest("Michael")
        self.assertEqual(0, len(self.room.guest_list))

    def test_remove_guest__doesnt_find_guest(self):
        self.room.add_guest(self.guest, self.bar)
        self.room.remove_guest("Marie")
        self.assertEqual(1, len(self.room.guest_list))

    def test_making_sure_room_playlist_zero(self):
        self.assertEqual(0, len(self.room.playlist))

    def test_add_song_to_room_playlist(self):
        self.room.add_song_to_room_playlist(self.song)
        self.assertEqual(1, len(self.room.playlist))

    def test_add_guest__no_room(self):
        self.room.add_room(self.room)
        self.room.add_guest(self.guest, self.bar)
        self.room.add_guest(self.guest, self.bar)
        self.room.add_guest(self.guest, self.bar)
        self.room.add_guest(self.guest, self.bar)
        self.assertEqual(2, len(self.room.guest_list))

    def test_guest_paid_entry(self):
        self.room.add_room(self.room)
        self.room.add_guest(self.guest, self.bar)
        self.assertEqual(40.0, self.guest.wallet)

    def test_fave_song_response(self):
        self.room.add_guest(self.guest, self.bar)
        self.room.add_song_to_room_playlist(self.song)
        self.assertEqual("Yaldy!", self.room.fave_song_response(self.guest))

    def test_cust_entry_added_to_bar_till(self):
        self.room.add_guest(self.guest, self.bar)
        self.assertEqual(110.00, self.bar.till)

    # def test_cust_spend_works(self):
    #     self.room.add_guest(self.guest, self.bar)
    #     self.guest.buy_drink(self.drink, self.bar, self.guest, self.room)
    #     self.guest.buy_food(self.food, self.bar, self.guest, self.room)
    #     self.assertEqual(22.70, self.room.guest_spend[self.guest])
        
