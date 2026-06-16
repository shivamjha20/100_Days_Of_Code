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

class Passenger(Person):
    def __init__(self, name):
        super().__init__(name)

    def request_ride(self, app, distance):
        app.book_ride(self, distance)

class Ride:
    def __init__(self, passenger, driver, distance):
        self.passenger = passenger
        self.driver = driver
        self.distance = distance
        self.fare = driver.rate_per_km * distance