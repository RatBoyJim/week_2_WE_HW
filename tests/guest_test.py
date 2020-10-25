import unittest

from classes.guest import *
from classes.room import *
from classes.drink import *
from classes.bar import *
from classes.food import *

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Michael", 50.00, "Anderson", "Believe", 38)

    def test_guest_has_name(self):
        self.assertEqual("Michael", self.guest.name)

    def test_guest_has_wallet(self):
        self.assertEqual(50.00, self.guest.wallet)

    def test_guest_has_booking_name(self):
        self.assertEqual("Anderson", self.guest.booking_name)

    def test_guest_has_fave(self):
        self.assertEqual("Believe", self.guest.fave)

    def test_guest_has_age(self):
        self.assertEqual(38, self.guest.age)

    def test_guest_can_buy_drink(self):
        bar = Bar("The Tubthumper", 100.00)
        drink = Drink("Vodka Drink", 6.50, 3)
        bar.add_drink_to_list(drink)
        self.guest.buy_drink(drink, bar)
        self.assertEqual(43.50, self.guest.wallet)

    def test_guest_is_refused_service_underage(self):
        bar = Bar("The Tubthumper", 100.00)
        drink = Drink("Vodka Drink", 6.50, 3)
        self.guest = Guest("Joseph Anderson", 20.00, "Anderson", "I Like To Move It", 5)
        bar.add_drink_to_list(drink)
        self.guest.buy_drink(drink, bar)
        self.assertEqual(100, bar.till)
        

    def test_guest_can_buy_drink_add_money_to_bar(self):
        bar = Bar("The Tubthumper", 100.00)
        drink = Drink("Vodka Drink", 6.50, 3)
        bar.add_drink_to_list(drink)
        self.guest.buy_drink(drink, bar)
        self.assertEqual(106.50, bar.till)

    def test_guest_drunkenness_goes_up(self):
        bar = Bar("The Tubthumper", 100.00)
        drink = Drink("Vodka Drink", 6.50, 3)
        bar.add_drink_to_list(drink)
        self.guest.buy_drink(drink, bar)
        self.assertEqual(3, self.guest.drunkenness)

    def test_guest_refused_service_too_drunk(self):
            bar = Bar("The Tubthumper", 100.00)
            drink = Drink("Vodka Drink", 6.50, 3)
            bar.add_drink_to_list(drink)
            self.guest.buy_drink(drink, bar)
            self.guest.buy_drink(drink, bar)
            self.guest.buy_drink(drink, bar)
            self.guest.buy_drink(drink, bar)
            self.guest.buy_drink(drink, bar)
            self.guest.buy_drink(drink, bar)
            self.assertEqual(17.50, self.guest.wallet)

    def test_guest_drunkenness_goes_down_with_food(self):
        bar = Bar("The Tubthumper", 100.00)
        drink = Drink("Vodka Drink", 6.50, 3)
        food = Food("Pizza", 7.20, 3)
        bar.add_drink_to_list(drink)
        bar.add_food_to_list(food)
        self.guest.buy_drink(drink, bar)
        self.guest.buy_drink(drink, bar)
        self.guest.buy_food(food, bar)
        self.assertEqual(3, self.guest.drunkenness)

    def test_guest_drunkenness_doesnt_go_below_zero(self):
        bar = Bar("The Tubthumper", 100.00)
        drink = Drink("Vodka Drink", 6.50, 3)
        food = Food("American Pie", 8.20, 8)
        bar.add_drink_to_list(drink)
        bar.add_food_to_list(food)
        self.guest.buy_drink(drink, bar)
        self.guest.buy_food(food, bar)
        self.assertEqual(0, self.guest.drunkenness)

    