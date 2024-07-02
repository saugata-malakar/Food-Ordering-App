class FoodOrderingApp:
    def __init__(self):
        self.menu = {
            1: {"name": "Burger", "price": 5.99},
            2: {"name": "Pizza", "price": 8.99},
            3: {"name": "Pasta", "price": 7.99},
            4: {"name": "Salad", "price": 4.99},
            5: {"name": "Fries", "price": 2.99}
        }
        self.order = []
    
    def display_menu(self):
        print("Menu:")
        for item_id, item in self.menu.items():
            print(f"{item_id}. {item['name']} - ${item['price']:.2f}")
    
    def take_order(self):
        while True:
            try:
                item_id = int(input("Enter the item number to order (0 to finish): "))
                if item_id == 0:
                    break
                if item_id in self.menu:
                    quantity = int(input(f"Enter the quantity for {self.menu[item_id]['name']}: "))
                    self.order.append((item_id, quantity))
                else:
                    print("Invalid item number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    def calculate_total(self):
        total = 0
        print("\nOrder Summary:")
        for item_id, quantity in self.order:
            item = self.menu[item_id]
            cost = item["price"] * quantity
            print(f"{item['name']} x{quantity} - ${cost:.2f}")
            total += cost
        print(f"Total: ${total:.2f}")
        return total
    
    def run(self):
        print("Welcome to the Food Ordering App!")
        while True:
            self.display_menu()
            self.take_order()
            if not self.order:
                print("No items ordered. Exiting.")
                break
            self.calculate_total()
            another_order = input("Would you like to place another order? (yes/no): ").lower()
            if another_order != "yes":
                print("Thank you for your order! Goodbye.")
                break
            self.order.clear()

# Run the application
if __name__ == "__main__":
    app = FoodOrderingApp()
    app.run()