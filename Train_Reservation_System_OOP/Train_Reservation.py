#
class Train:
    def __init__(self, train_no, train_name, total_seats):
        self.train_no = train_no
        self.train_name = train_name
        self.total_seats = total_seats
        self.available_seats = total_seats.copy()

    def book_seat(self, class_type):
        if class_type in self.available_seats and self.available_seats[class_type] > 0:
            self.available_seats[class_type] -= 1
            return True
        return False

    def cancel_seat(self, class_type):
        if class_type in self.available_seats:
            self.available_seats[class_type] += 1
            return True
        return False

    def get_train_info(self):
        return {
            "train_no": self.train_no,
            "train_name": self.train_name,
            "available_seats": self.available_seats
        }

class Reservation:
    reservation_counter = 1

    def __init__(self, passenger, train, class_type):
        self.reservation_id = f"R{Reservation.reservation_counter:03}"
        Reservation.reservation_counter += 1
        self.passenger = passenger
        self.train = train
        self.seat_class = class_type

    def generate_ticket(self):
        return {
            "reservation_id": self.reservation_id,
            "passenger_name": self.passenger.name,
            "train_no": self.train.train_no,
            "train_name": self.train.train_name,
            "seat_class": self.seat_class
        }

class Passenger:
    def __init__(self, passenger_id, name, age):
        self.passenger_id = passenger_id
        self.name = name
        self.age = age
        self.booked_train = None
        self.seat_class = None
        self.reservation = None

    def book_ticket(self, train, class_type):
        if self.booked_train is not None:
            return -1
        if train.book_seat(class_type):
            self.booked_train = train
            self.seat_class = class_type
            self.reservation = Reservation(self, train, class_type)
            return self.reservation
        return -1

    def cancel_ticket(self):
        if self.booked_train is None:
            return -1
        self.booked_train.cancel_seat(self.seat_class)
        self.booked_train = None
        self.seat_class = None
        self.reservation = None
        return "Cancellation successful"

    def get_ticket_details(self):
        if self.reservation is None:
            return -1
        return self.reservation.generate_ticket()



t1 = Train("T101", "Express Line", {"Economy": 3, "Business": 2})
t2 = Train("T102", "Coastal Ride", {"Economy": 2, "Business": 1})

p1 = Passenger("P101", "Alice", 25)
p2 = Passenger("P102", "Bob", 30)
p3 = Passenger("P103", "Charlie", 28)

res1 = p1.book_ticket(t1, "Economy")
res2 = p2.book_ticket(t1, "Economy")
res3 = p3.book_ticket(t1, "Economy")
res4 = p3.book_ticket(t1, "Economy") 

p1.cancel_ticket()

res5 = p3.book_ticket(t1, "Economy") 

print(p1.get_ticket_details())
print(p2.get_ticket_details())
print(p3.get_ticket_details())
print(t1.get_train_info())