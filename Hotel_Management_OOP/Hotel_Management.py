class Customer:
    counter = 5000

    def __init__(self, name, phone):
        self.customer_id = None
        self.name = name
        self.phone = phone

    def get_customer_id(self):
        return self.customer_id


class Room:
    counter = 100

    def __init__(self, room_price):
        Room.counter += 1
        self.room_id = Room.counter
        self.room_price = room_price
        self.is_available = True
        self.customer = None

    def calculate_room_rent(self, no_of_days):
        pass


class LuxuryRoom(Room):
    def calculate_room_rent(self, no_of_days):
        rent = self.room_price * no_of_days
        if no_of_days > 5:
            rent = rent - (0.05 * rent)
        return rent


class StandardRoom(Room):
    def calculate_room_rent(self, no_of_days):
        return self.room_price * no_of_days


class Hotel:
    def __init__(self, room_list):
        self.room_list = room_list

    def check_in(self, customer, room_type):
        for room in self.room_list:
            if room.is_available and room.__class__.__name__ == room_type:
                Customer.counter += 1
                customer.customer_id = Customer.counter
                room.customer = customer
                room.is_available = False
                return True
        return False

    def check_out(self, customer, no_of_days):
        for room in self.room_list:
            if room.customer == customer:
                rent = room.calculate_room_rent(no_of_days)
                room.customer = None
                room.is_available = True
                return rent
        return False


# ------------------- Testing -------------------

if __name__ == "__main__":
    # Create rooms
    r1 = LuxuryRoom(5000)
    r2 = LuxuryRoom(5000)
    r3 = StandardRoom(3000)

    hotel = Hotel([r1, r2, r3])

    # Create customer
    cust = Customer("Atharva", "9876543210")

    # Check-in
    if hotel.check_in(cust, "LuxuryRoom"):
        print("Check-in successful")
        print("Customer ID:", cust.get_customer_id())
    else:
        print("Check-in failed")

    # Check-out after 6 days
    rent = hotel.check_out(cust, 6)
    if rent:
        print("Total Rent:", rent)
    else:
        print("Check-out failed")
