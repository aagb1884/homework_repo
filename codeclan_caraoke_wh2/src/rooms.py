class Rooms:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.guestlist = []
        self.songlist = []

# - Add songs to rooms
    
    def add_guest_to_room(self, name):
        self.guestlist.append(name)

    def remove_guest_from_room(self, name):
        self.guestlist.remove(name)

    def add_song_to_room(self, song):
        self.songlist.append(song)