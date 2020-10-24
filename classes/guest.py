class Guest:
    def __init__(self, name, wallet, booking_name, fave):
        self.name = name
        self.wallet = wallet
        self.booking_name = booking_name
        self.fave = fave
        self.booking_list = []

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