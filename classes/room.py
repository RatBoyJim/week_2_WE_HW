class Room:
    def __init__(self, name, capacity, price):
        self.name = name
        self.capacity = capacity
        self.price = price
        self.room_list = []
        self.playlist = []
        self.guest_list = []
        
    def add_room(self, room):
        self.room_list.append(room)

    def add_guest(self, guest, bar):
        if len(self.guest_list) < self.capacity and guest.wallet >= self.price:
            guest.wallet -= self.price
            bar.till += self.price
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

    def add_song_to_room_playlist(self, song):
        self.playlist.append(song)

    def fave_song_response(self, guest):
        for song in self.playlist:
            if song.title == guest.fave:
                return "Yaldy!"


