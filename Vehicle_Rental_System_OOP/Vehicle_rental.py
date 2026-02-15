# ------------------------------
# Vehicle Rental System
# ------------------------------

# ------------------------------
# Vehicle Class
# ------------------------------
class Vehicle:
    def __init__(self, vehicle_id, vehicle_type, daily_rent):
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.daily_rent = daily_rent
        self.available = True

    def get_vehicle_id(self):
        return self.vehicle_id

    def get_vehicle_type(self):
        return self.vehicle_type

    def check_availability(self):
        return self.available

    def set_availability(self, status):
        self.available = status


# ------------------------------
# Customer Class
# ------------------------------
class Customer:
    def __init__(self, customer_id, customer_name):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.rented_vehicles = []  # list of tuples: (vehicle, days_rented)

    def get_customer_id(self):
        return self.customer_id

    def get_customer_name(self):
        return self.customer_name

    def rent_vehicle(self, vehicle, days):
        if not vehicle.check_availability() or days <= 0:
            return -1  # Vehicle not available or invalid days
        self.rented_vehicles.append((vehicle, days))
        vehicle.set_availability(False)
        total_rent = vehicle.daily_rent * days
        return total_rent

    def return_vehicle(self, vehicle):
        for rented in self.rented_vehicles:
            if rented[0] == vehicle:
                self.rented_vehicles.remove(rented)
                vehicle.set_availability(True)
                return "Vehicle returned successfully"
        return -1  # Vehicle not rented by customer


# ------------------------------
# RentalService Class
# ------------------------------
class RentalService:
    def __init__(self, service_name):
        self.service_name = service_name

    def process_rental(self, customer, vehicle, days):
        return customer.rent_vehicle(vehicle, days)

    def process_return(self, customer, vehicle):
        return customer.return_vehicle(vehicle)


# ------------------------------
# Example Usage
# ------------------------------

# Create Vehicles
v1 = Vehicle("V101", "Car", 2000)
v2 = Vehicle("V102", "Bike", 800)

# Create Customer
c1 = Customer(401, "Bob")

# Create Rental Service
service = RentalService("DriveEasy")

# Rent vehicles
print(service.process_rental(c1, v1, 3))   # 6000
print(service.process_rental(c1, v2, 2))   # 1600
print(service.process_rental(c1, v1, 1))   # -1 (already rented)

# Return vehicles
print(service.process_return(c1, v1))      # Vehicle returned successfully
print(service.process_return(c1, v1))      # -1 (already returned)

# Check vehicle availability
print("V1 available:", v1.check_availability())  # True
print("V2 available:", v2.check_availability())  # False
