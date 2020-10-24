import unittest

from classes.room import *

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Top o' the Pops", 2, 10)

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

    def test_check_in_guests():
        pass
    