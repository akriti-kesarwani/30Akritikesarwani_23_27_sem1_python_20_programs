class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price, quantity=1):
        if item in self.items:
            self.items[item]['quantity'] += quantity
        else:
            self.items[item] = {'price': price, 'quantity': quantity}

    def remove_item(self, item, quantity=1):
        if item in self.items:
            self.items[item]['quantity'] -= quantity
            if self.items[item]['quantity'] <= 0:
                del self.items[item]

    def calculate_total(self):
        total = 0
        for item, details in self.items.items():
            total += details['price'] * details['quantity']
        return total

    def display_cart(self):
        print("\nShopping Cart:")
        for item, details in self.items.items():
            print(f"{item} - Quantity: {details['quantity']}, Price: ${details['price']} each")
        print("\n")

# Example usage with user input:
cart = ShoppingCart()

while True:
    print("1. Add Item\n2. Remove Item\n3. Display Cart\n4. Calculate Total\n5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        item = input("Enter item name: ")
        price = float(input("Enter item price: "))
        quantity = int(input("Enter quantity: "))
        cart.add_item(item, price, quantity)
    elif choice == '2':
        item = input("Enter item name to remove: ")
        quantity = int(input("Enter quantity to remove: "))
        cart.remove_item(item, quantity)
    elif choice == '3':
        cart.display_cart()
    elif choice == '4':
        total_price = cart.calculate_total()
        print(f"Total Price: ${total_price}")
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
