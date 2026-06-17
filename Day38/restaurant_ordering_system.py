class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self, customer_name, table_number=None):
        self.customer_name = customer_name
        self.table_number = table_number
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"{item.name} added to {self.customer_name}'s order.")

    def calculate_total(self, tax_rate=0.05, discount=0):
        subtotal = sum(item.price for item in self.items)
        tax = subtotal * tax_rate
        total = subtotal + tax - discount
        return subtotal, tax, discount, total

    def show_receipt(self, tax_rate=0.05, discount=0):
        print(f"\n--- Receipt for {self.customer_name} ---")
        if self.table_number:
            print(f"Table: {self.table_number}")
        subtotal, tax, discount, total = self.calculate_total(tax_rate, discount)
        for item in self.items:
            print(f"- {item.name}: ₹{item.price}")
        print(f"\nSubtotal: ₹{subtotal}")
        print(f"Tax (GST {tax_rate*100:.0f}%): ₹{tax:.2f}")
        print(f"Discount: ₹{discount:.2f}")
        print(f"Total Bill: ₹{total:.2f}")
        print("-------------------------------\n")