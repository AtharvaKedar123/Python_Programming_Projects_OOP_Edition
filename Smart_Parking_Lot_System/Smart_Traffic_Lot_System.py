from datetime import datetime

class Vehicle:
    def __init__(self, plate):
        self.plate = plate

    def get_type(self):
        return "Generic"


class Car(Vehicle):
    def get_type(self):
        return "Car"


class Bike(Vehicle):
    def get_type(self):
        return "Bike"


class Truck(Vehicle):
    def get_type(self):
        return "Truck"


class VIPCar(Car):
    def get_type(self):
        return "VIP"


class ParkingSpot:
    def __init__(self, spot_id, spot_type):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.is_free = True
        self.vehicle = None

    def can_fit(self, vehicle):
        if isinstance(vehicle, Bike):
            return True
        if isinstance(vehicle, Car) and self.spot_type in ["CAR", "LARGE"]:
            return True
        if isinstance(vehicle, Truck) and self.spot_type == "LARGE":
            return True
        if isinstance(vehicle, VIPCar):
            return self.spot_type == "VIP"
        return False

    def park(self, vehicle):
        self.vehicle = vehicle
        self.is_free = False

    def remove(self):
        self.vehicle = None
        self.is_free = True


class Ticket:
    def __init__(self, vehicle, spot):
        self.vehicle = vehicle
        self.spot = spot
        self.entry_time = datetime.now()
        self.exit_time = None

    def close_ticket(self):
        self.exit_time = datetime.now()

    def calculate_fee(self):
        duration = (self.exit_time - self.entry_time).seconds / 60  # minutes

        rate = {
            "Bike": 10,
            "Car": 20,
            "VIP": 15,
            "Truck": 40
        }

        vtype = self.vehicle.get_type()
        return max(1, int(duration)) * rate.get(vtype, 20)


class ParkingLot:
    def __init__(self):
        self.spots = []
        self.tickets = {}

    def add_spot(self, spot):
        self.spots.append(spot)

    def find_spot(self, vehicle):
        # VIP gets priority spots first
        sorted_spots = sorted(self.spots, key=lambda s: "VIP" in s.spot_type)

        for spot in sorted_spots:
            if spot.is_free and spot.can_fit(vehicle):
                return spot
        return None

    def park_vehicle(self, vehicle):
        spot = self.find_spot(vehicle)
        if not spot:
            print("No available spot for", vehicle.get_type())
            return None

        spot.park(vehicle)
        ticket = Ticket(vehicle, spot)
        self.tickets[vehicle.plate] = ticket

        print(f"{vehicle.get_type()} parked at Spot {spot.spot_id}")
        return ticket

    def exit_vehicle(self, plate):
        if plate not in self.tickets:
            print("Invalid ticket")
            return

        ticket = self.tickets[plate]
        ticket.close_ticket()

        fee = ticket.calculate_fee()
        ticket.spot.remove()

        print(f"Vehicle {plate} exited. Fee = ₹{fee}")
        del self.tickets[plate]


# ---------------- DEMO ----------------
if __name__ == "__main__":
    lot = ParkingLot()

    # Add spots
    lot.add_spot(ParkingSpot(1, "CAR"))
    lot.add_spot(ParkingSpot(2, "LARGE"))
    lot.add_spot(ParkingSpot(3, "VIP"))

    # Vehicles
    v1 = Car("CAR123")
    v2 = Bike("BIKE456")
    v3 = VIPCar("VIP999")

    # Parking
    t1 = lot.park_vehicle(v1)
    t2 = lot.park_vehicle(v2)
    t3 = lot.park_vehicle(v3)

    # Simulate exit
    import time
    time.sleep(2)

    lot.exit_vehicle("CAR123")
    lot.exit_vehicle("BIKE456")