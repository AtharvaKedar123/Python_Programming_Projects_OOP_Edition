\# Hotel Management System



\## Problem Statement



A hotel wants to automate its room booking system using Object-Oriented Programming concepts.



Write a Python program to implement the class diagram given below.



---



\## Class Diagram



+--------------------------------------------------+

|                     Hotel                        |

+--------------------------------------------------+

| - room\_list : list<Room>                        |

+--------------------------------------------------+

| + \_\_init\_\_(room\_list)                           |

| + check\_in(customer, room\_type) : bool          |

| + check\_out(customer, no\_of\_days) : float/bool  |

+--------------------------------------------------+

&nbsp;               1

&nbsp;               |

&nbsp;               | Aggregation (HAS-A)

&nbsp;               | 0..\*

+--------------------------------------------------+

|                      Room                        |

+--------------------------------------------------+

| - counter : int {static} = 100                  |

| - room\_id : int                                 |

| - room\_price : float                            |

| - is\_available : bool                           |

| - customer : Customer                           |

+--------------------------------------------------+

| + \_\_init\_\_(room\_price)                          |

| + calculate\_room\_rent(no\_of\_days) : float       |

+--------------------------------------------------+

&nbsp;               1

&nbsp;               |

&nbsp;               | Association (Assigned to)

&nbsp;               | 0..1

+--------------------------------------------------+

|                    Customer                      |

+--------------------------------------------------+

| - counter : int {static} = 5000                 |

| - customer\_id : int                             |

| - name : str                                    |

| - phone : str                                   |

+--------------------------------------------------+

| + \_\_init\_\_(name, phone)                         |

| + get\_customer\_id() : int                       |

+--------------------------------------------------+



&nbsp;                       +----------------------+

&nbsp;                       |        Room          |

&nbsp;                       +----------------------+

&nbsp;                                ▲

&nbsp;                                │

&nbsp;             -----------------------------------------

&nbsp;             |                                       |

&nbsp;    +--------------------+                +----------------------+

&nbsp;    |     LuxuryRoom     |                |    StandardRoom      |

&nbsp;    +--------------------+                +----------------------+

&nbsp;    | + calculate\_room\_rent() (override)  |

&nbsp;    +-------------------------------------+





---



\## Class description



##### \### Customer class:



1\. Initialize static variable counter to 5000  

2\. customer\_id  

3\. name  

4\. phone  



---



##### \### Hotel class:



1\. room\_list: List of objects of rooms in the hotel  



2\. check\_in(customer, room\_type): Check-in the given customer based on details mentioned below.  



&nbsp;  1. Customer can check in only if the type of room desired by the customer is available.  

&nbsp;  2. If the room is available,  

&nbsp;     • Auto-generate customer.customer\_id starting from 5001  

&nbsp;     • Assign the customer to the available room  

&nbsp;     • Mark the room as not available  

&nbsp;     • Return True  

&nbsp;  3. Else, return False  



3\. check\_out(customer, no\_of\_days): Check-out the given customer based on details mentioned below.  



&nbsp;  1. Find out the room allocated to the given customer. If found,  

&nbsp;     • Identify the room rent based on type and number of days stayed by the customer  

&nbsp;     • Release the room, i.e., mark the room as available  

&nbsp;     • Remove customer from the room  

&nbsp;     • Return total room rent  

&nbsp;  2. Else, return False  



---



##### \### Room class:



1\. Initialize static variable counter to 100  

2\. room\_id  

3\. room\_price  

4\. is\_available  

5\. customer  



---



##### \### LuxuryRoom class:



calculate\_room\_rent(no\_of\_days): Calculate room rent  



1\. Calculate room rent based on room price and number of days  

2\. For stay of more than 5 days, provide 5% discount on total room rent  

3\. Return the final room rent  



---



##### \### StandardRoom class:



calculate\_room\_rent(no\_of\_days): Calculate room rent  



1\. Calculate room rent based on room price and number of days  

2\. Return the calculated room rent  



---



Perform case sensitive comparison.  

Create objects of Hotel class, invoke appropriate methods and test your program.

