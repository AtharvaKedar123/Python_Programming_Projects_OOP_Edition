import uuid

class MenuItem:
    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price

    def get_item_info(self):
        return {"item_id": self.item_id, "name": self.name, "price": self.price}


class Restaurant:
    def __init__(self, restaurant_id, name):
        self.restaurant_id = restaurant_id
        self.name = name
        self.menu_items = []

    def add_menu_item(self, item):
        self.menu_items.append(item)

    def get_menu(self):
        return [item.get_item_info() for item in self.menu_items]


class Order:
    def __init__(self, customer, restaurant, items):
        self.order_id = str(uuid.uuid4())[:8].upper()
        self.customer = customer
        self.restaurant = restaurant
        self.items = items
        self.total_amount = self.calculate_total()
        self.status = "Placed"

    def calculate_total(self):
        total = sum(item.price for item in self.items)
        if isinstance(self.customer, PremiumCustomer):
            total *= (1 - self.customer.discount_rate / 100)
        return total

    def update_status(self, status):
        if status in ["Placed", "Delivered", "Cancelled"]:
            self.status = status
            return True
        return False

    def get_order_details(self):
        return {
            "order_id": self.order_id,
            "customer": self.customer.name,
            "restaurant": self.restaurant.name,
            "items": [item.name for item in self.items],
            "total_amount": self.total_amount,
            "status": self.status
        }


class Customer:
    def __init__(self, customer_id, name, wallet_balance):
        self.customer_id = customer_id
        self.name = name
        self.wallet_balance = wallet_balance
        self.orders = []

    def place_order(self, restaurant, items):
        for item in items:
            if item not in restaurant.menu_items:
                return -1
        order = Order(self, restaurant, items)
        if self.wallet_balance >= order.total_amount:
            self.wallet_balance -= order.total_amount
            self.orders.append(order)
            return order.order_id
        return -1

    def get_order_history(self):
        return [order.get_order_details() for order in self.orders]

    def add_funds(self, amount):
        self.wallet_balance += amount
        return self.wallet_balance


class PremiumCustomer(Customer):
    def __init__(self, customer_id, name, wallet_balance, discount_rate):
        super().__init__(customer_id, name, wallet_balance)
        self.discount_rate = discount_rate

    def place_order(self, restaurant, items):
        for item in items:
            if item not in restaurant.menu_items:
                return -1
        order = Order(self, restaurant, items)
        if self.wallet_balance >= order.total_amount:
            self.wallet_balance -= order.total_amount
            self.orders.append(order)
            return order.order_id
        return -1


# ---------------- Sample Usage ----------------

m1 = MenuItem("MI101", "Pizza", 500)
m2 = MenuItem("MI102", "Burger", 200)
m3 = MenuItem("MI103", "Pasta", 300)

r1 = Restaurant("R101", "Pizza Palace")
r1.add_menu_item(m1)
r1.add_menu_item(m2)
r1.add_menu_item(m3)

c1 = Customer("C101", "Alice", 1000)
c2 = PremiumCustomer("C102", "Bob", 800, 10)

order1_id = c1.place_order(r1, [m1, m2])
order2_id = c2.place_order(r1, [m1, m3])

print("Alice Orders:")
print(c1.get_order_history())
print("Alice Wallet Balance:", c1.wallet_balance)

print("Bob Orders:")
print(c2.get_order_history())
print("Bob Wallet Balance:", c2.wallet_balance)

c2.add_funds(200)
print("Bob Added Funds:", c2.wallet_balance)

order3_id = c2.place_order(r1, [m2])
print("Bob Orders After Adding Funds:")
print(c2.get_order_history())
print("Bob Wallet Balance:", c2.wallet_balance)
