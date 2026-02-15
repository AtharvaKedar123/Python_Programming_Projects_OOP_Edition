class WeatherReading:
    def __init__(self, temperature, humidity, wind_speed):
        if not (-50 <= temperature <= 60) or not (0 <= humidity <= 100) or not (0 <= wind_speed <= 150):
            raise ValueError("Invalid weather reading")
        self.temperature = temperature
        self.humidity = humidity
        self.wind_speed = wind_speed

    def is_comfortable(self):
        return 18 <= self.temperature <= 25 and 30 <= self.humidity <= 60 and self.wind_speed <= 15

    def get_info(self):
        return {
            "temperature": self.temperature,
            "humidity": self.humidity,
            "wind_speed": self.wind_speed,
            "comfortable": self.is_comfortable()
        }


class StormAlert(WeatherReading):
    def __init__(self, temperature, humidity, wind_speed, alert_level):
        super().__init__(temperature, humidity, wind_speed)
        if not (1 <= alert_level <= 5):
            raise ValueError("Invalid alert level")
        self.alert_level = alert_level

    def get_info(self):
        info = super().get_info()
        info["alert_level"] = self.alert_level
        return info


class WeatherStation:
    def __init__(self):
        self.readings = []

    def add_reading(self, reading):
        if not isinstance(reading, WeatherReading):
            return -1
        self.readings.append(reading)

    def list_readings(self):
        return [reading.get_info() for reading in self.readings]

    def average_temperature(self):
        if not self.readings:
            return 0
        return sum(r.temperature for r in self.readings) / len(self.readings)

    def filter_comfortable(self):
        return [r.get_info() for r in self.readings if r.is_comfortable()]


# -------------------- Sample Usage --------------------

# Create readings
r1 = WeatherReading(20, 50, 10)
r2 = WeatherReading(22, 40, 12)
r3 = WeatherReading(30, 70, 20)  # Uncomfortable
s1 = StormAlert(18, 35, 14, 3)
s2 = StormAlert(25, 55, 10, 4)

# Create WeatherStation and add readings
station = WeatherStation()
station.add_reading(r1)
station.add_reading(r2)
station.add_reading(r3)
station.add_reading(s1)
station.add_reading(s2)

# List all readings
print("All Readings:")
for reading in station.list_readings():
    print(reading)

# Average temperature
print("\nAverage Temperature:", station.average_temperature())

# Comfortable readings
print("\nComfortable Readings:")
for reading in station.filter_comfortable():
    print(reading)
