class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, product):
        self.cart.append(product)
        print(f"{self.name} added {product.name} to cart.")

    def checkout(self):
        if not self.cart:
            print("Cart is empty!")
            return
        total = sum(p.price for p in self.cart)
        print(f"{self.name}'s total bill: ₹{total}")
        self.cart.clear()

class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def show_products(self):
        if not self.products:
            print("No products available.")
            return
        print(f"Products available in {self.name}:")
        for i, p in enumerate(self.products, start=1):
            print(f"{i}. {p.name} - ₹{p.price}")


# Menu-driven program
def main():
    store = Store("MiniMart")
    customer = Customer("Alice")

    while True:
        print("\n--- E-Commerce Menu ---")
        print("1. Add Product to Store")
        print("2. Show Products")
        print("3. Add Product to Cart")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter product name: ")
            price = int(input("Enter product price: "))
            store.add_product(Product(name, price))
            print(f"{name} added to store.")

        elif choice == "2":
            store.show_products()

        elif choice == "3":
            store.show_products()
            if store.products:
                index = int(input("Enter product number to add to cart: ")) - 1
                if 0 <= index < len(store.products):
                    customer.add_to_cart(store.products[index])
                else:
                    print("Invalid choice.")

        elif choice == "4":
            customer.checkout()

        elif choice == "5":
            print("Exiting... Thank you for shopping!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()