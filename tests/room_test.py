import unittest

from classes.room import *
from classes.guest import *

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Top o' the Pops", 2, 10)
        self.guest = Guest("Michael", 50.00, "Anderson", "Believe")

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
        guest = Guest("Marie", 100, "Anderson", "I'll Be There For You")
        self.room.add_guest(guest)
        self.assertEqual(1, len(self.room.guest_list))

    def test_find_guest__does_find_guest(self):
        self.room.add_guest(self.guest)
        self.assertEqual(True, self.room.find_guest("Michael"))

    def test_find_guest__doesnt_find_guest(self):
        self.room.add_guest(self.guest)
        self.assertEqual(False, self.room.find_guest("Marie"))

    def test_remove_guest__does_find_guest(self):
        self.room.add_guest(self.guest)
        self.room.remove_guest("Michael")
        self.assertEqual(0, len(self.room.guest_list))

    def test_remove_guest__doesnt_find_guest(self):
        self.room.add_guest(self.guest)
        self.room.remove_guest("Marie")
        self.assertEqual(1, len(self.room.guest_list))

    def test_check_in_guest(self):
        room = Room("Top o' the Pops", 2, 10)
        guest = Guest("Marie", 100, "Anderson", "I'll Be There For You")
        self.room.check_in_guest(room, guest)
        self.assertEqual(1, len(self.room.room_list))

    