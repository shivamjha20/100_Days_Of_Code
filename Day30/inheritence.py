'''Inheritance:-
->Allows a class to inherit attributes and methods from 
another class.'''
class Animal:
    def speak(self):
        print("This animal makes a sound.")

class Dog(Animal):   # inherits from Animal
    def speak(self):
        print("Woof!")

dog = Dog()
dog.speak()   # Woof!
