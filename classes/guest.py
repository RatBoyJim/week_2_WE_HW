class Guest:
    def __init__(self, name, wallet, booking_name, fave, age):
        self.name = name
        self.wallet = wallet
        self.booking_name = booking_name
        self.fave = fave
        self.age = age
        self.drunkenness = 0

    def buy_drink(self, drink, bar, guest, room):
        for item in bar.drinks:
            if item.name == drink.name and self.wallet >= item.price and self.age >= 18 and self.drunkenness < 15:
                self.wallet -= item.price
                bar.till += item.price
                room.guest_spend[guest] = room.guest_spend.get(guest, 0) + item.price
                self.drunkenness += item.alcohol_level

    def buy_food(self, food, bar, guest, room):
        for item in bar.food_list:
            if item.name == food.name and self.wallet >= item.price:
                self.wallet -= item.price
                bar.till += item.price
                room.guest_spend[guest] = room.guest_spend.get(guest, 0) + item.price
                if (self.drunkenness - item.rejuvenation_level) > 0:
                    self.drunkenness -= item.rejuvenation_level
                else:
                    self.drunkenness = 0
        
        

