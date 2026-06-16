class Person:
    def __init__(self, name):
        self.name = name

class Driver(Person):
    def __init__(self, name, vehicle, rate_per_km):
        super().__init__(name)
        self.vehicle = vehicle
        self.rate_per_km = rate_per_km
        self.available = True

    def toggle_availability(self):
        self.available = not self.available