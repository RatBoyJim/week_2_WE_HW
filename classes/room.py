class Room:
    def __init__(self, name, capacity, price):
        self.name = name
        self.capacity = capacity
        self.price = price
        self.room_list = []
        
    def add_room(self, room):
        self.room_list.append(room)