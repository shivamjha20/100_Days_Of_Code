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

    def show_details(self):
        print(f"\n--- Ride Details ---")
        print(f"Passenger: {self.passenger.name}")
        print(f"Driver: {self.driver.name} ({self.driver.vehicle})")
        print(f"Distance: {self.distance} km")
        print(f"Fare: ₹{self.fare}")
        print("-------------------\n")

class RideSharingApp:
    def __init__(self, name):
        self.name = name
        self.drivers = []
        self.passengers = []
        self.ride_history = []

    def add_driver(self, driver):
        self.drivers.append(driver)
        print(f"Driver {driver.name} added with vehicle {driver.vehicle}.")

    def add_passenger(self, passenger):
        self.passengers.append(passenger)
        print(f"Passenger {passenger.name} added.")

    def book_ride(self, passenger, distance):
        for driver in self.drivers:
            if driver.available:
                driver.toggle_availability()
                ride = Ride(passenger, driver, distance)
                ride.show_details()
                self.ride_history.append(ride)
                driver.toggle_availability()
                return ride
        print("No drivers available at the moment.")
        return None

    def show_ride_history(self):
        if not self.ride_history:
            print("No rides booked yet.")
            return
        print("\n=== Ride History ===")
        for i, ride in enumerate(self.ride_history, start=1):
            print(f"{i}. Passenger: {ride.passenger.name}, Driver: {ride.driver.name}, Distance: {ride.distance} km, Fare: ₹{ride.fare}")
        print("====================\n")

# Menu-driven program
def main():
    app = RideSharingApp("QuickRide")

    while True:
        print("\n--- Ride-Booking Menu ---")
        print("1. Add Driver")
        print("2. Add Passenger")
        print("3. Book Ride")
        print("4. Show Ride History")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter driver name: ")
            vehicle = input("Enter vehicle details: ")
            rate = int(input("Enter rate per km: "))
            app.add_driver(Driver(name, vehicle, rate))

        elif choice == "2":
            name = input("Enter passenger name: ")
            app.add_passenger(Passenger(name))

        elif choice == "3":
            passenger_name = input("Enter passenger name: ")
            distance = int(input("Enter distance (km): "))
            passenger = next((p for p in app.passengers if p.name == passenger_name), None)
            if passenger:
                passenger.request_ride(app, distance)
            else:
                print("Passenger not found!")

        elif choice == "4":
            app.show_ride_history()

        elif choice == "5":
            print("Exiting... Thank you for using QuickRide!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()