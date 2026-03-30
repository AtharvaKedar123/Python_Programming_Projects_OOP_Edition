
class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} is moving")

    def stop(self):
        print(f"{self.name} has stopped")

    def priority(self):
        return 0  



class Car(Vehicle):
    def priority(self):
        return 2

    def move(self):
        print(f"🚗 {self.name} (Car) is driving smoothly")


class Truck(Vehicle):
    def priority(self):
        return 1

    def move(self):
        print(f"🚚 {self.name} (Truck) is hauling goods slowly")


class Ambulance(Vehicle):
    def priority(self):
        return 3

    def move(self):
        print(f"🚑 {self.name} (Ambulance) is rushing with siren ON!")

    def stop(self):
        print(f"🚑 {self.name} ignores RED signal and keeps moving!")



class TrafficSignal:
    def __init__(self, color):
        self.color = color  

    def control_traffic(self, vehicles):
        print(f"\n🚦 Signal is {self.color}")

        vehicles_sorted = sorted(vehicles, key=lambda v: v.priority(), reverse=True)

        print("\nVehicle Order (by priority):")
        for v in vehicles_sorted:
            print(f"{v.name} → Priority {v.priority()}")

        print("\n--- Action ---")
        for v in vehicles_sorted:
            if self.color == "RED":
                if isinstance(v, Ambulance):
                    v.move()
                else:
                    v.stop()
            elif self.color == "GREEN":
                v.move()



if __name__ == "__main__":
    v1 = Car("Car A")
    v2 = Truck("Truck B")
    v3 = Ambulance("Ambulance X")
    v4 = Car("Car C")

    vehicles = [v1, v2, v3, v4]

    red_signal = TrafficSignal("RED")
    red_signal.control_traffic(vehicles)

    
    green_signal = TrafficSignal("GREEN")
    green_signal.control_traffic(vehicles)