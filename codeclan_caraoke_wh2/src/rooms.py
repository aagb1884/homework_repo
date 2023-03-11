class Rooms:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.guestlist = []
        self.songlist = []

    # - Check in guests to rooms/Check out guests from rooms
# - Add songs to rooms
    
    def add_guest_to_room(self, name):
        self.guestlist.append(name)

    def remove_guest_from_room(self, name):
        self.guestlist.remove(name)