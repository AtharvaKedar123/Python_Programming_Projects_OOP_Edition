#### Problem Statement







DriveEasy Rentals wants to automate their vehicle rental system. Customers can rent cars or bikes for a number of days. The system should track vehicles, customers, and rental transactions, including calculating rental charges and availability.  



You are required to implement this system using Python \*\*OOP concepts\*\*, following the class diagram and rules provided.



---



\## Class Diagram



&nbsp;                 +-------------------------------+

&nbsp;                 |           Vehicle             |

&nbsp;                 +-------------------------------+

&nbsp;                 | - vehicle\_id : str            |

&nbsp;                 | - vehicle\_type : str          |

&nbsp;                 | - daily\_rent : float          |

&nbsp;                 | - available : bool            |

&nbsp;                 +-------------------------------+

&nbsp;                 | + \_\_init\_\_(id, type, rent)    |

&nbsp;                 | + get\_vehicle\_id() : str      |

&nbsp;                 | + get\_vehicle\_type() : str    |

&nbsp;                 | + check\_availability() : bool|

&nbsp;                 | + set\_availability(status)    |

&nbsp;                 +-------------------------------+



&nbsp;                        1

&nbsp;                        |

&nbsp;                        | Aggregation (Has-A)

&nbsp;                        ◇

&nbsp;                        |

&nbsp;                        |

&nbsp;                 +-------------------------------+

&nbsp;                 |           Customer            |

&nbsp;                 +-------------------------------+

&nbsp;                 | - customer\_id : int           |

&nbsp;                 | - customer\_name : str         |

&nbsp;                 | - rented\_vehicles : list      |

&nbsp;                 +-------------------------------+

&nbsp;                 | + \_\_init\_\_(id, name)          |

&nbsp;                 | + get\_customer\_id() : int     |

&nbsp;                 | + get\_customer\_name() : str   |

&nbsp;                 | + rent\_vehicle(vehicle, days) |

&nbsp;                 | + return\_vehicle(vehicle)     |

&nbsp;                 +-------------------------------+



&nbsp;                        ^

&nbsp;                        |

&nbsp;                        | Association (Uses)

&nbsp;                        |

&nbsp;                 +-------------------------------+

&nbsp;                 |          RentalService        |

&nbsp;                 +-------------------------------+

&nbsp;                 | - service\_name : str          |

&nbsp;                 +-------------------------------+

&nbsp;                 | + \_\_init\_\_(name)              |

&nbsp;                 | + process\_rental(customer, vehicle, days) |

&nbsp;                 | + process\_return(customer, vehicle)       |

&nbsp;                 +-------------------------------+





---



\## Class Descriptions



#### \### Vehicle Class



\*\*Attributes:\*\*

\- `vehicle\_id` – Unique identifier for the vehicle.  

\- `vehicle\_type` – Either `"Car"` or `"Bike"`.  

\- `daily\_rent` – Cost per day.  

\- `available` – Boolean indicating availability.  



\*\*Methods:\*\*

1\. `\_\_init\_\_(id, type, rent)` – Initializes vehicle details, sets `available = True`.  

2\. `get\_vehicle\_id()` – Returns vehicle ID.  

3\. `get\_vehicle\_type()` – Returns vehicle type.  

4\. `check\_availability()` – Returns `True` if `available = True`.  

5\. `set\_availability(status)` – Updates vehicle availability.  



---

#### 

#### \### Customer Class



\*\*Attributes:\*\*

\- `customer\_id` – Unique ID of the customer.  

\- `customer\_name` – Name of the customer.  

\- `rented\_vehicles` – List of tuples `(Vehicle, days\_rented)` representing vehicles rented.  



\*\*Methods:\*\*

1\. `\_\_init\_\_(id, name)` – Initializes customer details and empty `rented\_vehicles`.  

2\. `get\_customer\_id()` – Returns customer ID.  

3\. `get\_customer\_name()` – Returns customer name.  

4\. `rent\_vehicle(vehicle, days)` – Rents a vehicle if:  

&nbsp;  - Vehicle is available.  

&nbsp;  - Number of days > 0.  

&nbsp;  Returns \*\*total rental amount\*\* if successful, else `-1`.  

5\. `return\_vehicle(vehicle)` – Returns vehicle:  

&nbsp;  - Removes from `rented\_vehicles`.  

&nbsp;  - Marks vehicle as available.  

&nbsp;  Returns `"Vehicle returned successfully"` or `-1` if vehicle not rented.  



---



#### \### RentalService Class



\*\*Attributes:\*\*

\- `service\_name` – Name of the rental service.  



\*\*Methods:\*\*

1\. `\_\_init\_\_(name)` – Initializes rental service name.  

2\. `process\_rental(customer, vehicle, days)` – Uses Customer and Vehicle objects to rent a vehicle. Returns total rental cost or `-1`.  

3\. `process\_return(customer, vehicle)` – Uses Customer and Vehicle objects to return vehicle. Returns `"Vehicle returned successfully"` or `-1`.  



---



\## Rules and Constraints



1\. Vehicle cannot be rented if \*\*not available\*\*.  

2\. Rental days must be \*\*positive integer\*\*.  

3\. Customer can rent multiple vehicles.  

4\. Upon returning, vehicle availability must be updated.  

5\. Aggregation is used between Customer and Vehicle.  

6\. RentalService uses association to handle rentals and returns.  



---



\## Expected Behavior



| Scenario | Output |

|----------|--------|

| Successful rental | Returns total rental amount (days × daily\_rent) |

| Renting unavailable vehicle | `-1` |

| Renting with invalid days | `-1` |

| Successful return | `"Vehicle returned successfully"` |

| Returning a vehicle not rented | `-1` |



---



\## Sample Usage



```python

\# Create Vehicles

v1 = Vehicle("V101", "Car", 2000)

v2 = Vehicle("V102", "Bike", 800)



\# Create Customer

c1 = Customer(401, "Bob")



\# Create Rental Service

service = RentalService("DriveEasy")



\# Rent vehicles

print(service.process\_rental(c1, v1, 3))   # 6000

print(service.process\_rental(c1, v2, 2))   # 1600

print(service.process\_rental(c1, v1, 1))   # -1 (already rented)



\# Return vehicle

print(service.process\_return(c1, v1))      # Vehicle returned successfully

print(service.process\_return(c1, v1))      # -1 (already returned)



\# Check vehicle availability

print(v1.check\_availability())             # True

print(v2.check\_availability())             # False

