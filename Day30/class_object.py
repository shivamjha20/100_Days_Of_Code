'''Class and Object:-
Class → blueprint for creating objects.
Object → instance of a class.'''
class Car:
    def __init__(self, brand, model):
        self.brand = brand   # attribute
        self.model = model

    def drive(self):         # method
        print(f"{self.brand} {self.model} is driving.")

# Create object
my_car = Car("Tesla", "Model S")
my_car.drive()

'''
->This code defines a class Car as a blueprint with attributes 
(brand, model) and a method (drive).
->The special __init__ constructor runs when you create an
object, storing values inside the object.
->The keyword self refers to the current object instance, 
allowing each object to keep its own data.
->Finally, calling my_car.drive() prints "Tesla Model S
 is driving.", showing how objects combine data + behavior.'''
