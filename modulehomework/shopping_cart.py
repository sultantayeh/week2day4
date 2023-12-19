class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)
        print(f"{item} has been added to the cart.")

    def remove(self, item_to_remove):
        if item_to_remove in self.items:
            self.items.remove(item_to_remove)
            print(f"{item_to_remove} has been removed from the cart.")
        else:
            print("Item not found in cart.")

    def show(self):
        if len(self.items) == 0:
            print("Your cart is empty.")
        else:
            print("Items in your cart:")
            for item in self.items:
                print(f"Item: {item}")
