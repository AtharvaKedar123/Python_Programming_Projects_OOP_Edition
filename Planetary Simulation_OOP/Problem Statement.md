Problem Statement

Create a **Planetary Simulation System** to manage **planets and their satellites**.  

The system must:  

1. Allow **creating planets** with a name, radius (in km), and mass (in kg).  
2. Allow **adding satellites** to planets. Each satellite has:  
   - Name  
   - Orbit radius (distance from planet in km)  
   - Orbital period (in days)  
3. Support **Artificial Satellites** with a specific purpose (Communication, Research, etc.).  
4. Determine whether a satellite is **stable**:  
   - Orbital period must be between 1 and 1000 days (inclusive).  
5. Allow **updating a satellite’s orbit** (orbit radius and orbital period).  
6. List **all satellites of a planet**, including stability and purpose (if artificial).  
7. Handle **multiple planets and satellites** using loops.  
8. Implement **aggregation** (planets have satellites) and **inheritance** (ArtificialSatellite inherits Satellite).  
9. Include validations using **if-else conditions**:
   - Cannot add a satellite if orbital period < 0 or orbit radius < 0.  
   - Stability must be calculated based on orbital period.  

---

## Class Diagram

                  +-----------------------------+
                  |          Planet            |
                  +-----------------------------+
                  | - name : str               |
                  | - radius : float           |
                  | - mass : float             |
                  | - satellites : list        |
                  +-----------------------------+
                  | + __init__(name, radius, mass) |
                  | + add_satellite(satellite) |
                  | + get_satellite_info()     |
                  +-----------------------------+

                         1
                         |
                         | Aggregation (Has-A)
                         ◇
                         |
                  +-----------------------------+
                  |        Satellite           |
                  +-----------------------------+
                  | - name : str               |
                  | - orbit_radius : float     |
                  | - orbital_period : float   |
                  +-----------------------------+
                  | + __init__(name, orbit_radius, orbital_period) |
                  | + is_stable() : bool       |
                  | + update_orbit(new_radius, new_period) |
                  | + get_info()               |
                  +-----------------------------+

                         ^
                         |
                         | Inheritance
                         |
                  +-----------------------------+
                  |    ArtificialSatellite     |
                  +-----------------------------+
                  | - purpose : str            |
                  +-----------------------------+
                  | + __init__(name, orbit_radius, orbital_period, purpose) |
                  | + get_info()               |
                  +-----------------------------+


---

## Class Methods in Detail

### **1. Planet Class**

**Attributes:**  
- `name` : str → Planet name  
- `radius` : float → Planet radius in km  
- `mass` : float → Planet mass in kg  
- `satellites` : list → List of Satellite objects  

**Methods:**  

1. `__init__(name, radius, mass)` → Initializes a new planet and empty satellite list.  
2. `add_satellite(satellite)` → Adds a satellite object to the planet.  
3. `get_satellite_info()` → Returns a list of dictionaries containing each satellite’s info.  

---

### **2. Satellite Class**

**Attributes:**  
- `name` : str → Satellite name  
- `orbit_radius` : float → Distance from planet in km  
- `orbital_period` : float → Orbital period in days  

**Methods:**  

1. `__init__(name, orbit_radius, orbital_period)` → Initialize satellite. Validate orbit_radius ≥ 0 and orbital_period ≥ 0.  
2. `is_stable()` → Returns True if 1 ≤ orbital_period ≤ 1000; else False.  
3. `update_orbit(new_radius, new_period)` → Update orbit radius and orbital period.  
4. `get_info()` → Return dictionary:
```python
{
  "name": self.name,
  "orbit_radius": self.orbit_radius,
  "orbital_period": self.orbital_period,
  "stable": self.is_stable()
}

3. ArtificialSatellite Class (Inherits Satellite)

Attributes:

    Inherits all Satellite attributes

    purpose : str → Purpose of satellite

Methods:

    __init__(name, orbit_radius, orbital_period, purpose) → Initialize artificial satellite.

    get_info() → Return dictionary:

{
  "name": self.name,
  "orbit_radius": self.orbit_radius,
  "orbital_period": self.orbital_period,
  "stable": self.is_stable(),
  "purpose": self.purpose
}

Rules & Validations

    Satellite orbital period and orbit radius must be ≥ 0.

    Stability: orbital period between 1 and 1000 days inclusive.

    Artificial satellites must store a purpose.

    Planets can have multiple satellites; satellites are linked to their planet.

    Display satellites using loops over planets and satellites.

    Use if-else conditions to validate orbit and period values.

Sample Usage

earth = Planet("Earth", 6371, 5.97e24)
mars = Planet("Mars", 3389, 6.42e23)

moon = Satellite("Moon", 384400, 27.3)
phobos = Satellite("Phobos", 9376, 0.3)
titan = ArtificialSatellite("TitanComm", 20000, 365, "Communication")

earth.add_satellite(moon)
mars.add_satellite(phobos)
earth.add_satellite(titan)

for planet in [earth, mars]:
    print(f"Planet: {planet.name}")
    for sat in planet.get_satellite_info():
        print(sat)

Expected Output (Sample)

Planet: Earth
{'name': 'Moon', 'orbit_radius': 384400, 'orbital_period': 27.3, 'stable': True}
{'name': 'TitanComm', 'orbit_radius': 20000, 'orbital_period': 365, 'stable': True, 'purpose': 'Communication'}
Planet: Mars
{'name': 'Phobos', 'orbit_radius': 9376, 'orbital_period': 0.3, 'stable': False}