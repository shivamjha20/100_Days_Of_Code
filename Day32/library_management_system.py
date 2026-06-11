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