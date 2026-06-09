'''Polymorphism:-
->Same method name, different behavior depending on the
object.'''
class Cat:
    def speak(self):
        print("Meow!")

class Dog:
    def speak(self):
        print("Woof!")

for animal in [Cat(), Dog()]:
    animal.speak()
