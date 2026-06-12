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

