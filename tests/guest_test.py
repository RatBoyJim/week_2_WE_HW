import unittest

from classes.guest import *

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Michael", 50.00, "Anderson", "Believe")

    def test_guest_has_name(self):
        self.assertEqual("Michael", self.guest.name)

    def test_guest_has_wallet(self):
        self.assertEqual(50.00, self.guest.wallet)

    def test_guest_has_booking_name(self):
        self.assertEqual("Anderson", self.guest.booking_name)

    def test_guest_has_fave(self):
        self.assertEqual("Believe", self.guest.fave)

    def test_add_guest_works(self):
        guest = Guest("Marie", 100, "Anderson", "I'll Be There For You")
        self.guest.add_guest(guest)
        self.assertEqual(1, len(self.guest.booking_list))

    def test_find_guest__does_find_guest(self):
        self.guest.add_guest(self.guest)
        self.assertEqual(True, self.guest.find_guest("Michael"))

    def test_find_guest__doesnt_find_guest(self):
        self.guest.add_guest(self.guest)
        self.assertEqual(False, self.guest.find_guest("Marie"))

    def test_remove_guest__does_find_guest(self):
        self.guest.add_guest(self.guest)
        self.guest.remove_guest("Michael")
        self.assertEqual(0, len(self.guest.booking_list))

    def test_remove_guest__doesnt_find_guest(self):
        self.guest.add_guest(self.guest)
        self.guest.remove_guest("Marie")
        self.assertEqual(1, len(self.guest.booking_list))