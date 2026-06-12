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