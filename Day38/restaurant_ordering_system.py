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

class Restaurant:
    def __init__(self, name, total_tables=10):
        self.name = name
        self.menu = []
        self.orders = []
        self.reserved_tables = {}
        self.total_tables = total_tables

    def add_menu_item(self, item):
        self.menu.append(item)
        print(f"{item.name} added to menu.")

    def show_menu(self):
        print(f"\n--- {self.name} Menu ---")
        for i, item in enumerate(self.menu, start=1):
            print(f"{i}. {item.name} - ₹{item.price}")

    def reserve_table(self, customer_name, table_number):
        if table_number in self.reserved_tables:
            print(f"Table {table_number} is already reserved.")
        elif table_number > self.total_tables or table_number < 1:
            print("Invalid table number.")
        else:
            self.reserved_tables[table_number] = customer_name
            print(f"Table {table_number} reserved for {customer_name}.")

    def create_order(self, customer_name):
        table_number = next((t for t, c in self.reserved_tables.items() if c == customer_name), None)
        order = Order(customer_name, table_number)
        self.orders.append(order)
        return order
    
    
# Menu-driven program
def main():
    restaurant = Restaurant("Foodie's Hub", total_tables=5)

    while True:
        print("\n--- Restaurant Menu ---")
        print("1. Add Menu Item")
        print("2. Show Menu")
        print("3. Reserve Table")
        print("4. Create Order")
        print("5. Add Item to Order")
        print("6. Show Receipt")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter item name: ")
            price = int(input("Enter item price: "))
            restaurant.add_menu_item(MenuItem(name, price))

        elif choice == "2":
            restaurant.show_menu()

        elif choice == "3":
            customer_name = input("Enter customer name: ")
            table_number = int(input("Enter table number: "))
            restaurant.reserve_table(customer_name, table_number)

        elif choice == "4":
            customer_name = input("Enter customer name: ")
            order = restaurant.create_order(customer_name)
            print(f"Order created for {customer_name}.")

        elif choice == "5":
            customer_name = input("Enter customer name: ")
            order = next((o for o in restaurant.orders if o.customer_name == customer_name), None)
            if order:
                restaurant.show_menu()
                index = int(input("Enter menu item number: ")) - 1
                if 0 <= index < len(restaurant.menu):
                    order.add_item(restaurant.menu[index])
                else:
                    print("Invalid choice.")
            else:
                print("Order not found.")

        elif choice == "6":
            customer_name = input("Enter customer name: ")
            order = next((o for o in restaurant.orders if o.customer_name == customer_name), None)
            if order:
                tax_rate = float(input("Enter GST rate (e.g., 0.05 for 5%): "))
                discount = float(input("Enter discount amount: "))
                order.show_receipt(tax_rate, discount)
            else:
                print("Order not found.")

        elif choice == "7":
            print("Exiting... Thank you for visiting Foodie's Hub!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()