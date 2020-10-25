import unittest
from classes.guest import *
from classes.bar import *
from classes.food import *

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food("American Pie", 7.20, 3)

    def food_has_name(self):
        self.assertEqual("American Pie", self.food.name)

    def test_food_has_price(self):
        self.assertEqual(7.20, self.food.price)

    def test_food_has_r_l(self):
        self.assertEqual(3, self.food.rejuvenation_level)