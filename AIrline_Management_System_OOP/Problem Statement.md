Problem Statement

SkyHigh Airlines wants to automate its reservation system. Passengers can book flights, and each flight has limited seats in different classes (Economy, Business). The system should track passengers, flight availability, seat classes, and payments.  

You are required to implement this system using Python **OOP concepts**, following the class diagram and rules provided.

---

## Class Diagram

                  +-------------------------------+
                  |            Flight             |
                  +-------------------------------+
                  | - flight_no : str             |
                  | - source : str                |
                  | - destination : str           |
                  | - seats : dict                |
                  |   ({"Economy": int,           |
                  |     "Business": int})         |
                  | - fare : dict                 |
                  |   ({"Economy": float,         |
                  |     "Business": float})       |
                  +-------------------------------+
                  | + __init__(flight_no, source, destination, seats, fare) |
                  | + get_flight_no() : str       |
                  | + check_seat_availability(class_type) : bool |
                  | + book_seat(class_type)       |
                  | + release_seat(class_type)    |
                  +-------------------------------+

                         1
                         |
                         | Aggregation (Has-A)
                         ◇
                         |
                         |
                  +-------------------------------+
                  |           Passenger           |
                  +-------------------------------+
                  | - passenger_id : int          |
                  | - passenger_name : str        |
                  | - wallet_balance : float      |
                  | - booked_flights : list       |
                  +-------------------------------+
                  | + __init__(id, name, balance) |
                  | + get_passenger_id() : int    |
                  | + get_passenger_name() : str  |
                  | + book_flight(flight, class_type) |
                  | + cancel_flight(flight, class_type) |
                  +-------------------------------+

                         ^
                         |
                         | Association (Uses)
                         |
                  +-------------------------------+
                  |         AirlineSystem         |
                  +-------------------------------+
                  | - airline_name : str          |
                  +-------------------------------+
                  | + __init__(name)              |
                  | + reserve_ticket(passenger, flight, class_type) |
                  | + cancel_ticket(passenger, flight, class_type)  |
                  +-------------------------------+


---

## Class Descriptions

### Flight Class

**Attributes:**
- `flight_no` – Unique flight number.  
- `source` – Departure city.  
- `destination` – Arrival city.  
- `seats` – Dictionary with seat availability for each class: `{"Economy": int, "Business": int}`.  
- `fare` – Dictionary with fare per class: `{"Economy": float, "Business": float}`.  

**Methods:**
1. `__init__(flight_no, source, destination, seats, fare)` – Initializes flight details.  
2. `get_flight_no()` – Returns flight number.  
3. `check_seat_availability(class_type)` – Returns `True` if seats available in class.  
4. `book_seat(class_type)` – Decrements seat count by 1.  
5. `release_seat(class_type)` – Increments seat count by 1.  

---

### Passenger Class

**Attributes:**
- `passenger_id` – Unique ID for the passenger.  
- `passenger_name` – Name of the passenger.  
- `wallet_balance` – Available balance for paying tickets.  
- `booked_flights` – List of tuples `(Flight, class_type)` representing bookings.  

**Methods:**
1. `__init__(id, name, balance)` – Initializes passenger with wallet and empty bookings.  
2. `get_passenger_id()` – Returns passenger ID.  
3. `get_passenger_name()` – Returns passenger name.  
4. `book_flight(flight, class_type)` – Books a seat if:  
   - Seat available in flight class.  
   - Passenger has enough wallet balance to pay fare.  
   Returns fare if successful, else `-1`.  
5. `cancel_flight(flight, class_type)` – Cancels booked flight:  
   - Releases seat in flight.  
   - Refunds 50% fare to wallet.  
   Returns `"Cancellation successful"` or `-1`.  

---

### AirlineSystem Class

**Attributes:**
- `airline_name` – Name of the airline.  

**Methods:**
1. `__init__(name)` – Initializes airline name.  
2. `reserve_ticket(passenger, flight, class_type)` – Uses Passenger and Flight objects to book a seat. Returns fare or `-1`.  
3. `cancel_ticket(passenger, flight, class_type)` – Uses Passenger and Flight objects to cancel a booking. Returns `"Cancellation successful"` or `-1`.  

---

## Rules and Constraints

1. Cannot book if **seat not available**.  
2. Passenger must have enough **wallet balance**.  
3. Refund on cancellation is **50% of fare**.  
4. Flight seat counts updated dynamically.  
5. Aggregation: Passenger “has-a” Flight.  
6. AirlineSystem uses association to handle bookings and cancellations.  

---

## Expected Behavior

| Scenario | Output |
|----------|--------|
| Successful booking | Returns fare amount |
| Booking with no seats | `-1` |
| Booking with insufficient balance | `-1` |
| Successful cancellation | `"Cancellation successful"` |
| Cancelling non-booked ticket | `-1` |

---

## Sample Usage

```python
# Create Flights
f1 = Flight("AI101", "Mumbai", "Delhi", {"Economy": 2, "Business": 1}, {"Economy": 5000, "Business": 12000})
f2 = Flight("AI102", "Delhi", "Bangalore", {"Economy": 3, "Business": 1}, {"Economy": 4000, "Business": 10000})

# Create Passengers
p1 = Passenger(701, "Alice", 15000)
p2 = Passenger(702, "Bob", 3000)

# Create Airline System
airline = AirlineSystem("SkyHigh Airlines")

# Reserve tickets
print(airline.reserve_ticket(p1, f1, "Economy"))   # 5000
print(airline.reserve_ticket(p1, f1, "Business"))  # 12000
print(airline.reserve_ticket(p2, f2, "Economy"))   # -1 (not enough balance)
print(airline.reserve_ticket(p1, f1, "Economy"))   # -1 (no seats available)

# Cancel tickets
print(airline.cancel_ticket(p1, f1, "Business"))   # Cancellation successful
print(airline.cancel_ticket(p1, f1, "Business"))   # -1 (already cancelled)