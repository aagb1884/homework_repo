class Venue:
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = rooms
        self.guests = []

# - Check in guests to rooms/Check out guests from rooms
# - Add songs to rooms
# who would be doing that irl? venue. so create venue. Hello venue.

# to check guests into/out of room
# need guest name
# need room name
# let's have all guests, rooms and songs in venue so they can be
# checked into rooms on request       

    def check_guest_into_venue(self, name):
        self.guests.append(name)

    def room_guest_count(self):
        return len(self.guests)