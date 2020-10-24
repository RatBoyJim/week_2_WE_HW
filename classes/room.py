class Room:
    def __init__(self, name, capacity, price):
        self.name = name
        self.capacity = capacity
        self.price = price
        self.room_list = {}
        self.playlist = []
        self.guest_list = []
        
    def add_room(self, room):
        self.room_list[room] = []

    def add_guest(self, guest):
        self.guest_list.append(guest)

    def find_guest(self, guest_to_find):
        for guest in self.guest_list:
            if guest.name == guest_to_find:
                return True
            else:
                return False
            
    def remove_guest(self, guest_to_remove):
        for guest in self.guest_list:
            if guest.name == guest_to_remove:
                self.guest_list.remove(guest)

    def check_in_guest(self, room, guest):
        self.room_list[room] = [guest]

