import datetime

# Base class
class Person:
    def __init__(self, name):
        self.name = name

# Member class
class Member(Person):
    def __init__(self, name, member_id):
        super().__init__(name)
        self.member_id = member_id
        self.borrowed_books = {}

    def borrow_book(self, book, library, days=7):
        if library.lend_book(book, self, days):
            due_date = datetime.date.today() + datetime.timedelta(days=days)
            self.borrowed_books[book] = due_date
            print(f"{self.name} borrowed {book.title}, due on {due_date}")

    def return_book(self, book, library):
        if book in self.borrowed_books:
            due_date = self.borrowed_books[book]
            today = datetime.date.today()
            if today > due_date:
                late_days = (today - due_date).days
                fine = late_days * library.fine_per_day
                print(f"{self.name} returned {book.title} late by {late_days} days. Fine: ₹{fine}")
            else:
                print(f"{self.name} returned {book.title} on time.")
            library.receive_book(book)
            del self.borrowed_books[book]  

# Book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author                  

# Library class
class Library:
    def __init__(self, name, fine_per_day=10):
        self.name = name
        self.books = []
        self.fine_per_day = fine_per_day

    def add_book(self, book):
        self.books.append(book)

    def lend_book(self, book, member, days):
        if book in self.books:
            self.books.remove(book)
            return True
        else:
            print(f"Sorry, {book.title} is not available.")
            return False

    def receive_book(self, book):
        self.books.append(book)

    def show_books(self):
        print(f"Books available in {self.name}:")
        for b in self.books:
            print(f"- {b.title} by {b.author}")

# Example usage
library = Library("City Library", fine_per_day=20)

book1 = Book("1984", "George Orwell")
book2 = Book("The Alchemist", "Paulo Coelho")

library.add_book(book1)
library.add_book(book2)

member1 = Member("Alice", "M101")

library.show_books()
member1.borrow_book(book1, library, days=5)   # borrow for 5 days
member1.return_book(book1, library)           # return (fine if late)