import unittest
from classes.drink import *

class TestDrink(unittest.TestCase):
    
    def setUp(self):
        self.drink = Drink("Whisky Drink", 5.50, 1)
    

    def test_drink_has_name(self):
        self.assertEqual("Whisky Drink", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(5.50, self.drink.price)

    def test_drink_has_alcohol_level(self):
        self.assertEqual(1, self.drink.alcohol_level)