Problem Statement

RailWayX wants to build a **Train Reservation & Management System** to automate train bookings and cancellations. The system should:

1. Maintain a list of **trains** with **different classes** (Economy, Business) and their seat availability.  
2. Allow **passengers** to **book tickets** for a train in a specific class.  
3. Prevent booking if **no seats are available** in the selected class.  
4. Allow passengers to **cancel their tickets**, freeing up seats.  
5. Generate **ticket details** with passenger info, train info, class booked, and reservation ID.  
6. Keep a **record of all passengers per train**.  
7. Support **multiple passengers booking and cancelling** tickets in a loop.  

The system should use **Python OOP concepts**: aggregation, association, and proper validations with **if-else and loops**.

---

## Class Diagram

                     +-------------------------------+
                     |            Train              |
                     +-------------------------------+
                     | - train_no : str              |
                     | - train_name : str            |
                     | - total_seats : dict          |
                     | - available_seats : dict      |
                     +-------------------------------+
                     | + __init__(train_no, name, total_seats) |
                     | + book_seat(class_type)       |
                     | + cancel_seat(class_type)     |
                     | + get_train_info()            |
                     +-------------------------------+

                         1
                         |
                         | Aggregation (Has-A)
                         ◇
                         |
                     +-------------------------------+
                     |          Passenger            |
                     +-------------------------------+
                     | - passenger_id : str          |
                     | - name : str                  |
                     | - age : int                   |
                     | - booked_train : Train        |
                     | - seat_class : str            |
                     +-------------------------------+
                     | + __init__(id, name, age)     |
                     | + book_ticket(train, class_type) |
                     | + cancel_ticket()             |
                     | + get_ticket_details()        |
                     +-------------------------------+

                         ^
                         |
                         | Association (Uses)
                         |
                     +-------------------------------+
                     |         Reservation           |
                     +-------------------------------+
                     | - reservation_id : str        |
                     | - passenger : Passenger       |
                     | - train : Train               |
                     | - seat_class : str            |
                     +-------------------------------+
                     | + __init__(passenger, train, class_type) |
                     | + generate_ticket()           |
                     +-------------------------------+


---

## Class Descriptions & Methods

### 1. Train Class
**Attributes:**  
- `train_no` – Unique train number  
- `train_name` – Train name  
- `total_seats` – Dictionary of total seats per class (e.g., `{"Economy": 50, "Business": 20}`)  
- `available_seats` – Tracks current available seats per class  

**Methods:**  
1. `__init__(train_no, train_name, total_seats)` – Initializes train and sets available seats = total seats.  
2. `book_seat(class_type)` – If seats available, reduce by 1 and return True; else return False.  
3. `cancel_seat(class_type)` – Increases available seats by 1.  
4. `get_train_info()` – Return train number, name, and available seats for each class.

---

### 2. Passenger Class
**Attributes:**  
- `passenger_id` – Unique passenger ID  
- `name` – Passenger name  
- `age` – Passenger age  
- `booked_train` – Train object (if booked)  
- `seat_class` – Class booked  

**Methods:**  
1. `__init__(id, name, age)` – Initializes passenger.  
2. `book_ticket(train, class_type)` –  
   - Call `train.book_seat(class_type)`  
   - If successful, store train and class in passenger and create a `Reservation` object  
   - Else return `-1`  
3. `cancel_ticket()` –  
   - Call `train.cancel_seat(class_type)`  
   - Remove booked_train and seat_class from passenger  
4. `get_ticket_details()` – Return dictionary with passenger name, train number, class, and reservation ID (if booked).

---

### 3. Reservation Class
**Attributes:**  
- `reservation_id` – Unique reservation ID (auto-generated, e.g., "R001")  
- `passenger` – Passenger object  
- `train` – Train object  
- `seat_class` – Class booked  

**Methods:**  
1. `__init__(passenger, train, class_type)` – Initializes reservation.  
2. `generate_ticket()` – Return dictionary with reservation ID, passenger name, train number, and seat class.

---

## Operations & Rules

1. Each passenger can **only book one seat per train**.  
2. Booking **fails** if no seats are available in selected class.  
3. Cancellation **frees up the seat** in the train.  
4. Reservations have **unique IDs** automatically generated.  
5. The system must support **looping through multiple passengers** for booking and cancellation.  
6. All operations must use **if-else checks** for validation.  
7. `Train.get_train_info()` must always show **current available seats**.  

---

## Sample Usage

```python
t1 = Train("T101", "Express Line", {"Economy": 3, "Business": 2})
t2 = Train("T102", "Coastal Ride", {"Economy": 2, "Business": 1})

p1 = Passenger("P101", "Alice", 25)
p2 = Passenger("P102", "Bob", 30)
p3 = Passenger("P103", "Charlie", 28)

res1 = p1.book_ticket(t1, "Economy")
res2 = p2.book_ticket(t1, "Economy")
res3 = p3.book_ticket(t1, "Economy")
res4 = p3.book_ticket(t1, "Economy") # Should fail, return -1

p1.cancel_ticket()

res5 = p3.book_ticket(t1, "Economy") # Should succeed now

print(p1.get_ticket_details())
print(p2.get_ticket_details())
print(p3.get_ticket_details())
print(t1.get_train_info())