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