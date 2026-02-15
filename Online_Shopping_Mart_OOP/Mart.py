class User:
    counter = 2000

    def __init__(self, name, email):
        User.counter += 1
        self.user_id = User.counter
        self.name = name
        self.email = email


class Product:
    counter = 5000

    def __init__(self, product_name, price, stock_quantity):
        Product.counter += 1
        self.product_id = Product.counter
        self.product_name = product_name
        self.price = price
        self.stock_quantity = stock_quantity

    def reduce_stock(self, quantity):
        if quantity <= self.stock_quantity:
            self.stock_quantity -= quantity
            return True
        else:
            return False


class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def calculate_total(self):
        return self.product.price * self.quantity


class Order:
    counter = 800

    def __init__(self, user):
        Order.counter += 1
        self.order_id = Order.counter
        self.user = user
        self.cart_items = []
        self.total_amount = 0

    def add_cart_item(self, cart_item):
        self.cart_items.append(cart_item)

    def calculate_order_total(self):
        total = 0
        for item in self.cart_items:
            total += item.calculate_total()

        if total >= 5000:
            total = total * 0.9  

        self.total_amount = total
        return self.total_amount


class ECommercePlatform:
    def __init__(self):
        self.users_list = []
        self.products_list = []
        self.orders_list = []

    def register_user(self, name, email):
        user = User(name, email)
        self.users_list.append(user)
        return user

    def add_product(self, product_name, price, stock_quantity):
        product = Product(product_name, price, stock_quantity)
        self.products_list.append(product)
        return product

    def find_user(self, user_id):
        for user in self.users_list:
            if user.user_id == user_id:
                return user
        return None

    def find_product(self, product_id):
        for product in self.products_list:
            if product.product_id == product_id:
                return product
        return None

    def create_order(self, user_id, product_id, quantity):
        user = self.find_user(user_id)
        product = self.find_product(product_id)

        if user and product:
            if product.reduce_stock(quantity):
                cart_item = CartItem(product, quantity)
                order = Order(user)
                order.add_cart_item(cart_item)
                final_amount = order.calculate_order_total()
                self.orders_list.append(order)
                return final_amount
            else:
                return False
        else:
            return False


platform = ECommercePlatform()

u1 = platform.register_user("Atharva", "atharva@gmail.com")
u2 = platform.register_user("Rahul", "rahul@gmail.com")

p1 = platform.add_product("Laptop", 45000, 10)
p2 = platform.add_product("Headphones", 3000, 5)

amount1 = platform.create_order(u1.user_id, p1.product_id, 1)
print("Order Amount:", amount1)

amount2 = platform.create_order(u2.user_id, p2.product_id, 2)
print("Order Amount:", amount2)

amount3 = platform.create_order(u2.user_id, p2.product_id, 10)
print("Order Status:", amount3)

print("Remaining Stock for Headphones:", p2.stock_quantity)
