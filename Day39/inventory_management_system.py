class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.product_id} - {self.name} | ₹{self.price} | Stock: {self.quantity}"
    
class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.product_id] = product
        print(f"Product {product.name} added.")

    def update_stock(self, product_id, quantity):
        if product_id in self.products:
            self.products[product_id].quantity += quantity
            print(f"Stock updated for {self.products[product_id].name}.")
        else:
            print("Product not found.")

    def show_inventory(self):
        print("\n--- Inventory ---")
        if not self.products:
            print("No products available.")
        for product in self.products.values():
            print(product)

class Sale:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
        self.total = product.price * quantity

    def process_sale(self):
        if self.product.quantity >= self.quantity:
            self.product.quantity -= self.quantity
            print(f"Sold {self.quantity} of {self.product.name}. Total: ₹{self.total}")
        else:
            print("Not enough stock!")

class InventorySystem:
    def __init__(self):
        self.inventory = Inventory()
        self.sales = []

    def run(self):
        while True:
            print("\n--- Inventory Management Menu ---")
            print("1. Add Product")
            print("2. Show Inventory")
            print("3. Update Stock")
            print("4. Process Sale")
            print("5. Show Sales Report")
            print("6. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                product_id = input("Enter product ID: ")
                name = input("Enter product name: ")
                price = int(input("Enter product price: "))
                quantity = int(input("Enter product quantity: "))
                product = Product(product_id, name, price, quantity)
                self.inventory.add_product(product)

            elif choice == "2":
                self.inventory.show_inventory()

            elif choice == "3":
                product_id = input("Enter product ID: ")
                quantity = int(input("Enter quantity to add: "))
                self.inventory.update_stock(product_id, quantity)

            elif choice == "4":
                product_id = input("Enter product ID: ")
                quantity = int(input("Enter quantity to sell: "))
                if product_id in self.inventory.products:
                    product = self.inventory.products[product_id]
                    sale = Sale(product, quantity)
                    sale.process_sale()
                    self.sales.append(sale)
                else:
                    print("Product not found.")

            elif choice == "5":
                if not self.sales:
                    print("No sales recorded yet.")
                else:
                    print("\n--- Sales Report ---")
                    for i, sale in enumerate(self.sales, start=1):
                        print(f"{i}. {sale.product.name} | Qty: {sale.quantity} | Total: ₹{sale.total}")
                    total_revenue = sum(s.total for s in self.sales)
                    print(f"Total Revenue: ₹{total_revenue}")

            elif choice == "6":
                print("Exiting... Goodbye!")
                break

            else:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    system = InventorySystem()
    system.run()