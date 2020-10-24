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