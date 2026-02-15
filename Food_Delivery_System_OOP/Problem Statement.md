Problem Statement



FoodieX is an online food delivery platform. They want a system that can:



1\. Manage \*\*restaurants\*\*, \*\*menu items\*\*, and \*\*customers\*\*.

2\. Allow customers to \*\*place orders\*\*, \*\*track order status\*\*, and \*\*make payments\*\*.

3\. Support \*\*special discounts\*\* for some customers.

4\. Keep a \*\*history of orders\*\* for both restaurants and customers.



You are required to implement the system using \*\*Python OOP\*\*, with \*\*inheritance, aggregation, and associations\*\*.



---



\## Class Diagram



&nbsp;                 +-------------------------------+

&nbsp;                 |           MenuItem            |

&nbsp;                 +-------------------------------+

&nbsp;                 | - item\_id : str               |

&nbsp;                 | - name : str                  |

&nbsp;                 | - price : float               |

&nbsp;                 +-------------------------------+

&nbsp;                 | + \_\_init\_\_(id, name, price)   |

&nbsp;                 | + get\_item\_info()             |

&nbsp;                 +-------------------------------+



&nbsp;                        1

&nbsp;                        |

&nbsp;                        | Aggregation (Has-A)

&nbsp;                        ◇

&nbsp;                        |

&nbsp;                 +-------------------------------+

&nbsp;                 |          Restaurant           |

&nbsp;                 +-------------------------------+

&nbsp;                 | - restaurant\_id : str         |

&nbsp;                 | - name : str                  |

&nbsp;                 | - menu\_items : list           |

&nbsp;                 +-------------------------------+

&nbsp;                 | + \_\_init\_\_(id, name)          |

&nbsp;                 | + add\_menu\_item(item)         |

&nbsp;                 | + get\_menu()                  |

&nbsp;                 +-------------------------------+



&nbsp;                        1

&nbsp;                        |

&nbsp;                        | Aggregation (Has-A)

&nbsp;                        ◇

&nbsp;                        |

&nbsp;                 +-------------------------------+

&nbsp;                 |           Customer            |

&nbsp;                 +-------------------------------+

&nbsp;                 | - customer\_id : str           |

&nbsp;                 | - name : str                  |

&nbsp;                 | - wallet\_balance : float      |

&nbsp;                 | - orders : list               |

&nbsp;                 +-------------------------------+

&nbsp;                 | + \_\_init\_\_(id, name, wallet)  |

&nbsp;                 | + place\_order(restaurant, items) |

&nbsp;                 | + get\_order\_history()         |

&nbsp;                 | + add\_funds(amount)           |

&nbsp;                 +-------------------------------+



&nbsp;                        ^

&nbsp;                        |

&nbsp;                        | Inheritance

&nbsp;                        |

&nbsp;                 +-------------------------------+

&nbsp;                 |        PremiumCustomer        |

&nbsp;                 +-------------------------------+

&nbsp;                 | - discount\_rate : float       |

&nbsp;                 +-------------------------------+

&nbsp;                 | + \_\_init\_\_(id, name, wallet, discount) |

&nbsp;                 | + place\_order(restaurant, items)      |

&nbsp;                 +-------------------------------+



&nbsp;                        ^

&nbsp;                        |

&nbsp;                        | Association (Uses)

&nbsp;                        |

&nbsp;                 +-------------------------------+

&nbsp;                 |            Order              |

&nbsp;                 +-------------------------------+

&nbsp;                 | - order\_id : str              |

&nbsp;                 | - customer : Customer         |

&nbsp;                 | - restaurant : Restaurant     |

&nbsp;                 | - items : list                |

&nbsp;                 | - total\_amount : float        |

&nbsp;                 | - status : str                |

&nbsp;                 +-------------------------------+

&nbsp;                 | + \_\_init\_\_(id, customer, restaurant, items) |

&nbsp;                 | + calculate\_total()           |

&nbsp;                 | + update\_status(status)       |

&nbsp;                 | + get\_order\_details()         |

&nbsp;                 +-------------------------------+





---



\## Class Descriptions \& Operations



#### \### 1. MenuItem Class

\*\*Attributes:\*\*

\- `item\_id` – Unique ID.

\- `name` – Name of food item.

\- `price` – Price of the item.



\*\*Methods:\*\*

1\. `\_\_init\_\_(id, name, price)` – Initialize item.

2\. `get\_item\_info()` – Return `{item\_id, name, price}`.



---



#### \### 2. Restaurant Class

\*\*Attributes:\*\*

\- `restaurant\_id` – Unique ID.

\- `name` – Restaurant name.

\- `menu\_items` – List of MenuItem objects.



\*\*Methods:\*\*

1\. `\_\_init\_\_(id, name)` – Initialize restaurant.

2\. `add\_menu\_item(item)` – Add MenuItem object to menu.

3\. `get\_menu()` – Return all items in menu.



---



#### \### 3. Customer Class

\*\*Attributes:\*\*

\- `customer\_id` – Unique ID.

\- `name` – Customer name.

\- `wallet\_balance` – Balance for payments.

\- `orders` – List of Order objects.



\*\*Methods:\*\*

1\. `\_\_init\_\_(id, name, wallet)` – Initialize customer.

2\. `place\_order(restaurant, items)` – Place an order:

&nbsp;  - Total = sum of item prices.

&nbsp;  - Deduct from wallet.

&nbsp;  - Create Order object with status `"Placed"`.

&nbsp;  - Return order ID or `-1` if insufficient balance.

3\. `get\_order\_history()` – Return all past orders.

4\. `add\_funds(amount)` – Increase wallet balance.



---



#### \### 4. PremiumCustomer Class (Inherits Customer)

\*\*Attributes:\*\*

\- `discount\_rate` – Discount in percentage (e.g., 10%).



**\*\*Methods:\*\***

1\. `\_\_init\_\_(id, name, wallet, discount)` – Initialize with discount.

2\. `place\_order(restaurant, items)` – Same as Customer, \*\*apply discount\*\* to total.



---



#### \### 5. Order Class

\*\*Attributes:\*\*

\- `order\_id` – Unique ID.

\- `customer` – Customer object.

\- `restaurant` – Restaurant object.

\- `items` – List of MenuItem objects.

\- `total\_amount` – Total after discount (if any).

\- `status` – `"Placed"` by default; can be `"Delivered"` or `"Cancelled"`.



**\*\*Methods:\*\***

1\. `\_\_init\_\_(id, customer, restaurant, items)` – Initialize order.

2\. `calculate\_total()` – Sum item prices; apply discount if PremiumCustomer.

3\. `update\_status(status)` – Change status.

4\. `get\_order\_details()` – Return dictionary of order info.



---



\## Operations \& Rules



1\. Customer can only place order if \*\*wallet balance ≥ total amount\*\*.

2\. \*\*PremiumCustomer\*\* gets discount before deduction.

3\. Order status must be `"Placed"`, `"Delivered"`, or `"Cancelled"`.

4\. Menu items must belong to the restaurant when ordering.

5\. Adding funds updates wallet.

6\. Customers maintain \*\*order history\*\*; restaurants track \*\*menu items only\*\*.



---



\## Sample Usage



```python

\# Create menu items

m1 = MenuItem("MI101", "Pizza", 500)

m2 = MenuItem("MI102", "Burger", 200)



\# Create restaurants

r1 = Restaurant("R101", "Pizza Palace")

r1.add\_menu\_item(m1)

r1.add\_menu\_item(m2)



\# Create customers

c1 = Customer("C101", "Alice", 1000)

c2 = PremiumCustomer("C102", "Bob", 800, 10)



\# Customer places order

order1 = c1.place\_order(r1, \[m1, m2])

order2 = c2.place\_order(r1, \[m1])



\# Access order details

print(c1.get\_order\_history())

print(c2.get\_order\_history())

