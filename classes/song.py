from classes.room import *

class Song:
    def __init__(self, title, artist, genre, duration):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.duration = duration
        self.playlist = []
        

    def add_song(self, song):
        self.playlist.append(song)

    def find_song(self, title_to_find):
        for song in self.playlist:
            if song.title == title_to_find:
                return True
            else:
                return False
            
    def remove_song(self, title_to_remove):
        for song in self.playlist:
            if song.title == title_to_remove:
                self.playlist.remove(song)