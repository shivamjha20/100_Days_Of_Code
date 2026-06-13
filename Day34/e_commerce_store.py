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