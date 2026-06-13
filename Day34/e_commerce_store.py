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