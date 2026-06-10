# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")