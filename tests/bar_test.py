import unittest
from classes.bar import *
from classes.drink import *
from classes.food import *

class TestBar(unittest.TestCase):
    
    def setUp(self):
        self.bar = Bar("The Tubthumping Bar", 100.00)
    

    def test_bar_has_name(self):
        self.assertEqual("The Tubthumping Bar", self.bar.name)

    def test_till_has_money(self):
        self.assertEqual(100.00, self.bar.till)

    def test_add_drink_to_list(self):
        drink = Drink("Vodka Drink", 6.50, 3)
        self.bar.add_drink_to_list(drink)
        self.assertEqual(1, self.bar.drinks_list_count())

    def test_add_food_to_list(self):
        food = Food("Soul Food", 5.50, 2)
        self.bar.add_food_to_list(food)
        self.assertEqual(1, self.bar.food_list_count())

    def test_stock_count_works(self):
        drink = Drink("Vodka Drink", 6.50, 3)
        self.bar.add_drink_to_list(drink)
        self.bar.add_drink_to_list(drink)
        self.bar.add_drink_to_list(drink)
        self.assertEqual(3, self.bar.drinks[drink])

    def test_stock_value(self):
        drink = Drink("Vodka Drink", 6.50, 3)
        self.bar.add_drink_to_list(drink)
        self.bar.add_drink_to_list(drink)
        self.assertEqual(13.00, self.bar.stock_value())