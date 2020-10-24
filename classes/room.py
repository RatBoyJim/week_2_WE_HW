class Room:
    def __init__(self, name, capacity, price):
        self.name = name
        self.capacity = capacity
        self.price = price
        self.room_list = []
        self.playlist = []
        self.booking_list = []
        
    def add_room(self, room):
        self.room_list.append(room)

    def add_guest(self, guest):
        self.booking_list.append(guest)

    def find_guest(self, guest_to_find):
        for guest in self.booking_list:
            if guest.name == guest_to_find:
                return True
            else:
                return False
            
    def remove_guest(self, guest_to_remove):
        for guest in self.booking_list:
            if guest.name == guest_to_remove:
                self.booking_list.remove(guest)