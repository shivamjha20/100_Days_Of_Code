# Room class
class Room:
    def __init__(self, room_number, room_type, price):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.is_booked = False

    def book(self):
        if not self.is_booked:
            self.is_booked = True
            return True
        return False

    def release(self):
        self.is_booked = False

# Guest class
class Guest:
    def __init__(self, name, guest_id):
        self.name = name
        self.guest_id = guest_id

# Booking class
class Booking:
    def __init__(self, guest, room, nights):
        self.guest = guest
        self.room = room
        self.nights = nights
        self.total_cost = room.price * nights

    def show_details(self):
        print(f"Booking Details:\nGuest: {self.guest.name}\nRoom: {self.room.room_number} ({self.room.room_type})\nNights: {self.nights}\nTotal Cost: ₹{self.total_cost}")
        
# Hotel class
class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def show_available_rooms(self):
        print(f"Available rooms in {self.name}:")
        for room in self.rooms:
            if not room.is_booked:
                print(f"- Room {room.room_number} ({room.room_type}) ₹{room.price}")

    def book_room(self, guest, room_number, nights):
        for room in self.rooms:
            if room.room_number == room_number and not room.is_booked:
                if room.book():
                    booking = Booking(guest, room, nights)
                    booking.show_details()
                    return booking
        print("Room not available.")
        return None